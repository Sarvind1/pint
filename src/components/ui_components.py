import streamlit as st

def show_loading_spinner(text="Loading pin..."):
    """Display a loading spinner with custom text"""
    st.markdown(f"""
        <div class="loading-container">
            <div class="spinner"></div>
            <div class="loading-text">{text}</div>
        </div>
    """, unsafe_allow_html=True)

def show_app_header():
    """Display the application header"""
    st.markdown("""
        <div class="app-header">
            <h1>📌 Pinterest Embed Viewer</h1>
            <p>Browse through your curated Pinterest pins with style</p>
        </div>
    """, unsafe_allow_html=True)

def show_pin_counter(current_index, total_pins):
    """Display the pin counter"""
    st.markdown(f"""
        <div class="pin-counter">
            Pin {current_index + 1} of {total_pins}
        </div>
    """, unsafe_allow_html=True)

def show_pin_info(title, description):
    """Display pin information"""
    st.markdown(f"""
        <div class="pin-info">
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)




def show_error_message(message):
    """Display an error message"""
    st.markdown(f"""
        <div class="error-message">
            {message}
        </div>
    """, unsafe_allow_html=True)

def show_info_message(title, message, additional_info=None):
    """Display an information message"""
    st.markdown(f"""
        <div class="info-message">
            <h3>{title}</h3>
            <p>{message}</p>
            {f'<p style="margin-top: 1rem; font-size: 0.9rem; color: #6c757d;">{additional_info}</p>' if additional_info else ''}
        </div>
    """, unsafe_allow_html=True)

def show_tip_message(message):
    """Display a tip message"""
    st.markdown(f"""
        <div class="tip-message">
            💡 <strong>Tip:</strong> {message}
        </div>
    """, unsafe_allow_html=True) 