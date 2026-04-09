def get_styles():
    return """
    html, body, .stApp {
        background: #fff !important;
        color: #222 !important;
        font-family: 'Inter', 'Arial', sans-serif !important;
    }
    .main .block-container {
        padding: 1.5rem 0.5rem 0.5rem 0.5rem !important;
        max-width: 600px !important;
        margin: 0 auto !important;
        background: none !important;
        box-shadow: none !important;
        border-radius: 0 !important;
    }
    .top-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 0.5rem;
        font-size: 1.1rem;
        font-weight: 600;
        letter-spacing: 0.01em;
    }
    .pin-counter {
        font-size: 0.95rem;
        color: #888;
        font-weight: 400;
        background: none;
        border-radius: 0;
        padding: 0;
        margin-left: 1rem;
    }
    .nav-row {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .nav-btn {
        background: none;
        border: none;
        color: #444;
        font-size: 1.6rem;
        padding: 0.2em 0.6em;
        border-radius: 50%;
        transition: background 0.15s;
        cursor: pointer;
        line-height: 1;
    }
    .nav-btn:hover {
        background: #f0f0f0;
        color: #111;
    }
    .pin-info {
        flex: 1 1 0;
        min-width: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5em;
        font-size: 1.05rem;
        font-weight: 500;
        color: #222;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .pin-info strong {
        font-weight: 700;
        margin-right: 0.4em;
        color: #111;
    }
    .pin-info span {
        color: #666;
        font-weight: 400;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        display: inline-block;
        max-width: 60vw;
    }
    .stHtml {
        margin: 0.5rem 0 0 0 !important;
        padding: 0 !important;
        background: none !important;
        border-radius: 0 !important;
        box-shadow: none !important;
    }
    .stHtml iframe {
        border-radius: 0 !important;
        border: 1px solid #eee !important;
        margin: 0 auto !important;
        display: block !important;
    }
    .info-message, .error-message, .tip-message {
        background: none;
        color: #888;
        border: none;
        font-size: 0.95rem;
        padding: 0.25rem 0;
        margin: 0.25rem 0;
        border-radius: 0;
        text-align: center;
    }
    .loading-container {
        background: none;
        padding: 0.5rem 0;
        margin: 0.25rem 0;
        text-align: center;
    }
    .spinner {
        width: 18px;
        height: 18px;
        border-width: 2px;
    }
    @media (max-width: 600px) {
        .main .block-container {
            padding: 0.5rem !important;
        }
        .pin-info span {
            max-width: 40vw;
        }
    }
    """.strip() 