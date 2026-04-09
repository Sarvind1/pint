# Pinterest Pin Viewer

A Streamlit-based web application for browsing and viewing Pinterest pins with an elegant carousel interface. Features responsive design, intelligent caching, and smooth navigation through your curated pin collection.

## Features

- **Interactive Pin Carousel** — Navigate through pins with previous/next controls
- **Responsive Design** — Automatically adapts layout for mobile and desktop devices
- **Smart Caching** — Avoids redundant API calls with in-memory pin cache (limit: 15)
- **Styled Interface** — Clean, modern UI with custom CSS styling
- **Pinterest oEmbed Integration** — Fetches official pin embeds with automatic dimension adjustment
- **Pin Counter** — Track your position in the carousel
- **Error Handling** — Graceful error messages for invalid pins or network issues

## Tech Stack

- **Streamlit** — Web app framework
- **Python 3** — Core language
- **requests** — HTTP client for Pinterest oEmbed API
- **pandas** — Data manipulation (CSV handling)

## Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd pinterest-pin-viewer
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run pint.py
   ```

The app will open in your browser at `http://localhost:8501`

## Usage

1. Add Pinterest pin URLs to `pins.csv` in the following format:
   ```
   pin_url
   https://www.pinterest.com/pin/123456789/
   https://www.pinterest.com/pin/987654321/
   ```

2. Use the carousel navigation buttons to browse through pins
3. The app will automatically fetch and display the pin embeds
4. Pin dimensions are adjusted responsively based on device type

## Dependencies

- `streamlit` — Web framework
- `requests` — API requests
- `pandas` — CSV data handling

See `requirements.txt` for exact versions.