import streamlit as st
import requests
import streamlit.components.v1 as components
import pandas as pd
from collections import OrderedDict
import re
from src.styles.styles import get_styles

# Set page config
st.set_page_config(
    page_title="Pinterest Embed Viewer",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Apply minimal styles
st.markdown(f"<style>{get_styles()}</style>", unsafe_allow_html=True)

# Session state
if 'pin_cache' not in st.session_state:
    st.session_state.pin_cache = OrderedDict()
if 'carousel_index' not in st.session_state:
    st.session_state.carousel_index = 0

# --- Utility functions ---
def fetch_pin_embed(pin_url):
    if pin_url in st.session_state.pin_cache:
        return st.session_state.pin_cache[pin_url]
    oembed_url = f"https://www.pinterest.com/oembed.json?url={pin_url}"
    try:
        response = requests.get(oembed_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        st.session_state.pin_cache[pin_url] = data
        if len(st.session_state.pin_cache) > 15:
            st.session_state.pin_cache.popitem(last=False)
        return data
    except Exception:
        return None

def extract_dimensions(html):
    width_match = re.search(r'width="(\d+)"', html)
    height_match = re.search(r'height="(\d+)"', html)
    if width_match and height_match:
        return int(width_match.group(1)), int(height_match.group(1))
    return None, None

def create_iframe_html(src, width, height):
    return f'<iframe src="{src}" height="{height}" width="{width}" frameborder="0" allowfullscreen></iframe>'

def adjust_iframe_dimensions(html, target_width=600):
    original_width, original_height = extract_dimensions(html)
    if not original_width or not original_height:
        return html, 400
    aspect_ratio = original_height / original_width
    new_height = int(target_width * aspect_ratio)
    src_match = re.search(r'src="([^"]+)"', html)
    if not src_match:
        return html, 400
    modified_html = create_iframe_html(
        src=src_match.group(1),
        width=target_width,
        height=new_height
    )
    return modified_html, new_height

def navigate_pin(direction, pins_df):
    if direction == 'next':
        st.session_state.carousel_index = (st.session_state.carousel_index + 1) % len(pins_df)
    else:
        st.session_state.carousel_index = (st.session_state.carousel_index - 1) % len(pins_df)

# --- Data loading ---
# (No file uploader for minimalism)
csv_path = "pins.csv"
try:
    pins_df = pd.read_csv(csv_path)
except FileNotFoundError:
    pins_df = None

# --- UI ---
# Top bar: App title (left), pin counter (right)
st.markdown('<div class="top-bar">'
    '<span>Pinterest Embed Viewer</span>'
    f'<span class="pin-counter">{f"Pin {st.session_state.carousel_index+1} of {len(pins_df)}" if pins_df is not None else ""}</span>'
    '</div>', unsafe_allow_html=True)

if pins_df is not None and {'url', 'title', 'description'}.issubset(pins_df.columns):
    pin = pins_df.iloc[st.session_state.carousel_index]
    # Main row: [Prev] [Pin info] [Next]
    st.markdown('<div class="nav-row">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 8, 1])
    with col1:
        if st.button("◀", key="prev", use_container_width=True):
            navigate_pin('previous', pins_df)
            st.rerun()
    with col3:
        if st.button("▶", key="next", use_container_width=True):
            navigate_pin('next', pins_df)
            st.rerun()
    with col2:
        st.markdown(f'<div class="pin-info"><strong>{pin["title"]}</strong>· <span>{pin["description"]}</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    # Pinterest embed
    pin_data = fetch_pin_embed(pin['url'])
    if pin_data:
        try:
            modified_html, new_height = adjust_iframe_dimensions(pin_data["html"], target_width=600)
            components.html(modified_html, height=new_height)
        except Exception:
            st.info("Unable to display pin embed.")
    else:
        st.info("Failed to load the pin. Try the next one.")
else:
    st.info("Please ensure pins.csv exists and has columns: url, title, description.")