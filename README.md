# Pinterest Embed Viewer

A Streamlit web application for browsing and displaying Pinterest pins as embedded iframes. Load pins from a CSV file and view them with responsive, mobile-friendly layouts.

## Features

- **Fetch Pinterest Embeds**: Automatically fetch pin embed code using the Pinterest oEmbed API
- **Responsive Layouts**: Adapts iframe dimensions for desktop and mobile devices while maintaining aspect ratio
- **Pin Caching**: Caches fetched embeds to reduce API calls and improve performance
- **CSV-Based Pin List**: Load pins from a CSV file for easy management
- **Clean UI**: Minimalist design with custom styling, header, pin counter, and navigation controls

## Tech Stack

- **Streamlit** - Web app framework
- **Python 3.7+** - Core language
- **pandas** - CSV data handling
- **requests** - HTTP requests for oEmbed API

## Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd pinterest-embed-viewer
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare your pins CSV** (optional)
   - Create a `pins.csv` file with your Pinterest pin URLs

5. **Run the app**
   ```bash
   streamlit run pint.py
   ```

The app will open in your browser at `http://localhost:8501`.

## Usage

1. The app loads pins from `pins.csv` and displays them one at a time
2. Use navigation buttons (◀ ▶) to browse through pins
3. The app automatically fetches embed data from Pinterest and adjusts iframe sizes for your device
4. Hover to see pin titles and descriptions
5. The app caches fetches to avoid redundant API calls

## File Structure

- `pint.py` - Main Streamlit application
- `src/utils/pin_utils.py` - Utilities for iframe handling and device detection
- `src/styles/styles.py` - Custom CSS styling
- `src/components/ui_components.py` - Reusable UI components
- `pins.csv` - Your Pinterest pin URLs (ignored in git)
- `requirements.txt` - Python dependencies