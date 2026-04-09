# Pinterest Embed Viewer

A Streamlit application for browsing and displaying Pinterest pins in an interactive carousel viewer. Fetch pins from Pinterest's oEmbed API, cache them for performance, and view them with responsive design optimized for both mobile and desktop.

## Features

- **Pin Carousel**: Navigate through pins with intuitive prev/next controls
- **Embed Caching**: Intelligent caching (max 15 pins) for faster loading
- **Responsive Design**: Auto-adjusts iframe dimensions for mobile and desktop viewing
- **Dimension Extraction**: Automatically extracts and preserves pin aspect ratios
- **Clean UI**: Custom-styled interface with minimal distractions
- **Pin Counter**: Track your position in the carousel

## Tech Stack

- **Streamlit** - Web application framework
- **Pandas** - Data handling (CSV loading)
- **Requests** - HTTP client for oEmbed API
- **Python 3.8+**

## Setup

1. Clone the repository and navigate to it:
   ```bash
   cd pinterest-embed-viewer
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Prepare a CSV file (`pins.csv`) with Pinterest pin URLs:
   ```
   pin_url
   https://www.pinterest.com/pin/123456789/
   https://www.pinterest.com/pin/987654321/
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run pint.py
   ```

3. Open your browser to the local Streamlit URL (typically `http://localhost:8501`) and navigate through pins using the arrow buttons.

## Project Structure

```
.
├── pint.py                      # Main Streamlit application
├── pins.csv                     # Pin URLs (data file)
├── requirements.txt             # Python dependencies
├── src/
│   ├── components/ui_components.py   # Reusable UI components
│   ├── styles/styles.py              # Custom CSS styling
│   └── utils/pin_utils.py            # Utility functions for pin handling
└── README.md
```

## Requirements

See `requirements.txt` for the complete list. Key dependencies:
- streamlit
- requests
- pandas