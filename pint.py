import streamlit as st
import requests
import streamlit.components.v1 as components
import pandas as pd
from collections import OrderedDict
import time
import re

# st.set_page_config(page_title="Pinterest Embed Viewer", layout="centered")

# Enhanced CSS for strict centering and layout control with UI-friendly container
st.markdown("""
    <style>
    /* Override Streamlit's default container */
    .main > div {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    
    /* Set background for entire page */
    .stApp {
        min-height: 100vh;
        background: linear-gradient(135deg, #eadf66 0%, #4ba279 100%);
    }
    
    /* Style the main Streamlit container */
    .main .block-container {
        padding: 2rem 1rem !important;
        max-width: 900px !important;
        background: rgba(255, 255, 255, 0.95) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 20px !important;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        margin: 2rem auto !important;
    }

    .app-header {
        text-align: center;
        margin-bottom: 2rem;
        color: #2c3e50;
    }
    
    .app-header h1 {
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .app-header p {
        font-size: 1.1rem;
        color: #6c757d;
        margin: 0.5rem 0 0 0;
        font-weight: 400;
    }

    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        font-size: 1.1em;
        font-weight: 600;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
        border: 2px solid transparent;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }

    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
    }

    .pin-info {
        padding: q rem;
        background: linear-gradient(135deg, #a9f9fa 0%, #21e2e2 100%);
        border-radius: 16px;
        margin: 1.5rem 0;
        box-shadow: 0 8px 30px rgba(0,0,0,0.1);
        width: 100%;
        box-sizing: border-box;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    .pin-info h3 {
        color: #2c3e50;
        font-weight: 700;
        margin-top: 0;
        font-size: 1.4rem;
    }

    .pin-info p {
        color: #6c757d;
        line-height: 1.6;
        margin-bottom: 0;
        font-size: 1rem;
    }

    .nav-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
        width: 100%;
        margin: 1rem 0;
    }

    .nav-buttons {
        display: flex;
        width: 100%;
        max-width: 400px;
        justify-content: center;
        gap: 1rem;
    }

    .pin-counter {
        text-align: center;
        margin: 1rem 0;
        font-size: 1.1em;
        font-weight: 600;
        color: #495057;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        display: inline-block;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }

    /* Pinterest embed container styling */
    .stHtml {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        background: white !important;
        border-radius: 16px !important;
        box-shadow: 0 8px 30px rgba(0,0,0,0.1) !important;
        padding: 1rem !important;
        margin: 1rem 0 !important;
        overflow: hidden !important;
    }

    /* Target the iframe created by Streamlit components.html */
    .stHtml iframe {
        margin: 0 auto !important;
        display: block !important;
        border-radius: 12px !important;
    }

    /* Center Pinterest content inside iframe */
    .stHtml iframe body {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        text-align: center !important;
    }

    /* Pinterest embed spans centering */
    span[data-pin-href] {
        display: block !important;
        margin: 0 auto !important;
        text-align: center !important;
        max-width: fit-content !important;
    }

    /* Target Pinterest PIN classes */
    [class*="PIN_"] {
        margin: 0 auto !important;
        text-align: center !important;
        display: inline-block !important;
    }

    /* Pinterest overlay spans */
    span[class*="PIN_"][class*="overlay"] {
        position: relative !important;
        display: inline-block !important;
        margin: 0 auto !important;
        text-align: center !important;
    }

    /* Force centering on any Pinterest container */
    .stHtml > div {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
    }

    .loading-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 3rem;
        margin: 2rem 0;
        width: 100%;
        background: rgba(255, 255, 255, 0.5);
        border-radius: 16px;
        backdrop-filter: blur(5px);
    }

    .spinner {
        border: 4px solid rgba(102, 126, 234, 0.2);
        border-top: 4px solid #667eea;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        animation: spin 1s linear infinite;
        margin-bottom: 1rem;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .loading-text {
        color: #6c757d;
        font-size: 1rem;
        font-weight: 500;
    }

    .info-message {
        text-align: center;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 12px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
    }

    .tip-message {
        text-align: center;
        margin-top: 2 rem;
        color: #6c757d;
        font-size: 0.95rem;
        background: rgba(255, 255, 255, 0.7);
        padding: 1rem;
        border-radius: 12px;
        backdrop-filter: blur(5px);
    }

    .error-message {
        background: rgba(255, 107, 107, 0.1);
        border: 1px solid rgba(255, 107, 107, 0.3);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        color: #721c24;
        margin: 1rem 0;
    }

    /* Ensure Streamlit's default markdown and column elements are centered */
    .stMarkdown, .stColumns {
        text-align: center;
    }

    /* Responsive adjustments */
    @media (min-width: 968px) {
        .nav-container {
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
        }
        .nav-buttons {
            width: auto;
            max-width: none;
        }
        .pin-counter {
            order: 0;
        }
    }

    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem 0.5rem !important;
            margin: 1rem auto !important;
            border-radius: 15px !important;
        }

        .app-header h1 {
            font-size: 1.8rem;
        }

        .app-header p {
            font-size: 1rem;
        }

        .pin-info {
            padding: 1rem;
            margin: 0.75rem 0;
        }

        .pin-info h3 {
            font-size: 1.2rem;
        }

        .pin-info p {
            font-size: 0.9rem;
        }

        .stButton>button {
            height: 2.8em;
            font-size: 0.95em;
            margin: 0.25rem 0;
        }

        .nav-buttons {
            flex-direction: column;
            gap: 0.5rem;
            width: 100%;
        }

        .pin-counter {
            font-size: 0.9em;
            padding: 0.5rem 1rem;
            margin: 0.5rem 0;
        }

        .stHtml {
            padding: 0.5rem !important;
            margin: 0.5rem 0 !important;
        }

        .stHtml iframe {
            width: 100% !important;
            max-width: 100% !important;
        }

        .loading-container {
            padding: 1.5rem;
            margin: 1rem 0;
        }

        .spinner {
            width: 40px;
            height: 40px;
        }

        .loading-text {
            font-size: 0.9rem;
        }

        .info-message {
            padding: 1.5rem;
            margin: 0.75rem 0;
        }

        .tip-message {
            font-size: 0.85rem;
            padding: 0.75rem;
            margin-top: 1rem;
        }

        .error-message {
            padding: 0.75rem;
            margin: 0.75rem 0;
            font-size: 0.9rem;
        }
    }

    /* Additional mobile optimizations */
    @media (max-width: 480px) {
        .main .block-container {
            padding: 0.75rem 0.25rem !important;
            margin: 0.5rem auto !important;
        }

        .app-header h1 {
            font-size: 1.5rem;
        }

        .stButton>button {
            height: 2.5em;
            font-size: 0.9em;
        }

        .pin-info {
            padding: 0.75rem;
        }

        .pin-info h3 {
            font-size: 1.1rem;
        }

        .pin-info p {
            font-size: 0.85rem;
        }
    }

    /* Ensure proper touch targets on mobile */
    @media (hover: none) {
        .stButton>button {
            min-height: 44px; /* Minimum touch target size */
        }

        .nav-buttons button {
            padding: 12px 20px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for caching and navigation
if 'pin_cache' not in st.session_state:
    st.session_state.pin_cache = OrderedDict()
if 'carousel_index' not in st.session_state:
    st.session_state.carousel_index = 0
if 'loading' not in st.session_state:
    st.session_state.loading = False

def show_loading_spinner(text="Loading pin..."):
    st.markdown(f"""
        <div class="loading-container">
            <div class="spinner"></div>
            <div class="loading-text">{text}</div>
        </div>
    """, unsafe_allow_html=True)

def adjust_iframe_dimensions(html, target_width=650):
    """Adjust iframe dimensions while maintaining aspect ratio"""
    try:
        # Check if we're on mobile (screen width <= 768px)
        is_mobile = False
        try:
            # Get the current viewport width using JavaScript
            js = """
            <script>
                window.mobileCheck = window.innerWidth <= 768;
            </script>
            """
            components.html(js, height=0)
            is_mobile = True
        except:
            pass

        # Set target width based on device
        target_width = 350 if is_mobile else 650

        # Extract original width and height using regex
        width_match = re.search(r'width="(\d+)"', html)
        height_match = re.search(r'height="(\d+)"', html)
        
        if width_match and height_match:
            original_width = int(width_match.group(1))
            original_height = int(height_match.group(1))
            
            # Calculate new height maintaining aspect ratio
            aspect_ratio = original_height / original_width
            new_height = int(target_width * aspect_ratio)
            
            # Create new iframe HTML with all necessary attributes
            modified_html = f'<iframe src="{re.search(r"src=\"([^\"]+)\"", html).group(1)}" height="{new_height}" width="{target_width}" frameborder="0" scrolling="yes" allowfullscreen></iframe>'
            
            return modified_html, new_height
        return html, 400  # Return original HTML and default height if dimensions not found
    except Exception as e:
        st.error(f"Error adjusting dimensions: {str(e)}")
        return html, 400

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
    except (requests.exceptions.RequestException, KeyError) as e:
        st.error(f"Failed to load pin: {str(e)}")
        return None

def preload_pins(pins_df, current_index):
    total_pins = len(pins_df)
    for i in range(1, 4):
        next_index = (current_index + i) % total_pins
        next_pin = pins_df.iloc[next_index]
        if next_pin['url'] not in st.session_state.pin_cache:
            try:
                fetch_pin_embed(next_pin['url'])
            except:
                pass

def navigate_pin(direction):
    st.session_state.loading = True
    if direction == 'next':
        st.session_state.carousel_index = (st.session_state.carousel_index + 1) % len(pins_df)
    else:
        st.session_state.carousel_index = (st.session_state.carousel_index - 1) % len(pins_df)

# File uploader for custom CSV
uploaded_file = None
# st.file_uploader("Upload pins.csv", type=["csv"])

# Load pins from CSV
csv_path = "pins.csv"
pins_df = None

if uploaded_file is not None:
    pins_df = pd.read_csv(uploaded_file)
else:
    try:
        pins_df = pd.read_csv(csv_path)
    except FileNotFoundError:
        st.warning(f"No '{csv_path}' found. Upload a CSV to use the carousel.")

# App header
st.markdown("""
    <div class="app-header">
        <h1>📌 Pinterest Embed Viewer</h1>
        <p>Browse through your curated Pinterest pins with style</p>
    </div>
""", unsafe_allow_html=True)

if pins_df is not None:
    if not {'url', 'title', 'description'}.issubset(pins_df.columns):
        st.markdown("""
            <div class="error-message">
                <strong>⚠️ CSV Format Error</strong><br>
                CSV must have columns: url, title, description
            </div>
        """, unsafe_allow_html=True)
    else:
        total_pins = len(pins_df)
        pin = pins_df.iloc[st.session_state.carousel_index]

        # Pin counter
        st.markdown(f"""
            <div class="pin-counter">
                Pin {st.session_state.carousel_index + 1} of {total_pins}
            </div>
        """, unsafe_allow_html=True)

        # Pin information
        st.markdown(f"""
            <div class="pin-info">
                <h3>{pin['title']}</h3>
                <p>{pin['description']}</p>
            </div>
        """, unsafe_allow_html=True)

        # Navigation
        st.markdown('<div class="nav-container">', unsafe_allow_html=True)
        st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Previous", key="prev", use_container_width=True):
                navigate_pin('previous')
                st.rerun()
        with col2:
            if st.button("Next ➡️", key="next", use_container_width=True):
                navigate_pin('next')
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Embed display
    
        preload_pins(pins_df, st.session_state.carousel_index)
        pin_data = fetch_pin_embed(pin['url'])
        if pin_data:
            st.markdown('<div class="iframe-container" >', unsafe_allow_html=True)
            try:
                # Adjust dimensions while maintaining aspect ratio
                modified_html, new_height = adjust_iframe_dimensions(pin_data["html"])
                
                components.html(
                    modified_html,
                    height=new_height*0.9,
                    scrolling=True
                )
            except Exception as e:
                st.error(f"Error displaying pin: {str(e)}")
                st.markdown("""
                    <div class="error-message">
                        Unable to display pin embed. Please try refreshing or skip to the next pin.
                    </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="error-message">
                    Failed to load the pin. Please try the next one.
                </div>
            """, unsafe_allow_html=True)
            if st.button("Skip to Next Pin", key="skip", use_container_width=True):
                navigate_pin('next')
                st.rerun()

    # Navigation hint
        st.markdown("""
            <div class="tip-message">
                💡 <strong>Tip:</strong> Use the navigation buttons to browse through your curated pins
            </div>
        """, unsafe_allow_html=True)

else:
    st.markdown("""
        <div class="info-message">
            <h3>🚀 Getting Started</h3>
            <p>Please upload a <code>pins.csv</code> file or ensure it exists in the same directory to start viewing pins.</p>
            <p style="margin-top: 1rem; font-size: 0.9rem; color: #6c757d;">
                Your CSV should contain columns: <strong>url</strong>, <strong>title</strong>, and <strong>description</strong>
            </p>
        </div>
    """, unsafe_allow_html=True)