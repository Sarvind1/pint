import re
import streamlit as st
import streamlit.components.v1 as components
import requests
from collections import OrderedDict

def get_device_type():
    """Detect if the current device is mobile based on viewport width"""
    try:
        js = """
        <script>
            window.mobileCheck = window.innerWidth <= 768;
        </script>
        """
        components.html(js, height=0)
        return True
    except:
        return False

def extract_dimensions(html):
    """Extract width and height from iframe HTML"""
    width_match = re.search(r'width="(\d+)"', html)
    height_match = re.search(r'height="(\d+)"', html)
    
    if width_match and height_match:
        return int(width_match.group(1)), int(height_match.group(1))
    return None, None

def create_iframe_html(src, width, height):
    """Create iframe HTML with specified dimensions"""
    return f'<iframe src="{src}" height="{height}" width="{width}" frameborder="0" scrolling="yes" allowfullscreen></iframe>'

def adjust_iframe_dimensions(html, target_width=650):
    """Adjust iframe dimensions while maintaining aspect ratio"""
    try:
        # Determine device type and target width
        is_mobile = get_device_type()
        target_width = 350 if is_mobile else 650

        # Extract original dimensions
        original_width, original_height = extract_dimensions(html)
        if not original_width or not original_height:
            return html, 400

        # Calculate new dimensions
        aspect_ratio = original_height / original_width
        new_height = int(target_width * aspect_ratio)
        
        # Extract source URL and create new iframe
        src_match = re.search(r'src="([^"]+)"', html)
        if not src_match:
            return html, 400
            
        modified_html = create_iframe_html(
            src=src_match.group(1),
            width=target_width,
            height=new_height
        )
        
        return modified_html, new_height

    except Exception as e:
        st.error(f"Error adjusting dimensions: {str(e)}")
        return html, 400

def fetch_pin_embed(pin_url):
    """Fetch Pinterest embed data for a given URL"""
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
    except (requests.exceptions.RequestException, KeyError) as e:
        st.error(f"Failed to load pin: {str(e)}")
        return None

def preload_pins(pins_df, current_index):
    """Preload next few pins for smoother navigation"""
    total_pins = len(pins_df)
    for i in range(1, 4):
        next_index = (current_index + i) % total_pins
        next_pin = pins_df.iloc[next_index]
        if next_pin['url'] not in st.session_state.pin_cache:
            try:
                fetch_pin_embed(next_pin['url'])
            except:
                pass 