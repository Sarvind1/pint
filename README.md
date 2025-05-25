# Pinterest Embed Viewer

A Streamlit application that displays Pinterest pins in a carousel format with a clean, mobile-first interface.

## Project Structure

```
Pinterest/
├── pint.py          # Main application file
├── pins.csv         # CSV file containing pin data
└── README.md        # Project documentation
```

## Features

1. **Pin Display**
   - Responsive Pinterest pin embeds
   - Mobile-first design
   - Centered layout with clean UI
   - Loading states and error handling

2. **Navigation**
   - Previous/Next navigation buttons
   - Pin counter display
   - Smooth transitions between pins
   - Background preloading of next pins

3. **Data Management**
   - CSV-based pin data storage
   - Pin caching for better performance
   - Error handling and recovery

## CSV Structure

The `pins.csv` file should contain the following columns:
- `url`: Pinterest pin URL
- `title`: Pin title
- `description`: Pin description

## Technical Implementation

### Core Components

1. **State Management**
   ```python
   - pin_cache: Caches pin data for better performance
   - carousel_index: Tracks current pin position
   - loading: Manages loading states
   ```

2. **Key Functions**
   ```python
   - fetch_pin_embed(): Retrieves pin data from Pinterest API
   - preload_pins(): Background loading of next pins
   - navigate_pin(): Handles pin navigation
   - show_loading_spinner(): Displays loading state
   ```

3. **UI Components**
   ```python
   - Content Container: Centers all content
   - Navigation Buttons: Previous/Next controls
   - Pin Counter: Shows current position
   - Loading Spinner: Visual feedback during loading
   ```

### Styling

The application uses custom CSS for:
- Responsive layout
- Mobile-first design
- Loading animations
- Error states
- Button interactions
- Centered content

## Usage

1. Prepare your `pins.csv` file with the required columns
2. Run the application:
   ```bash
   streamlit run pint.py
   ```

## Error Handling

The application includes:
- API request timeout handling
- Pin loading error recovery
- Skip functionality for failed pins
- User-friendly error messages

## Performance Optimizations

1. **Caching**
   - Pin data caching
   - Cache size management
   - Background preloading

2. **Loading States**
   - Visual feedback during transitions
   - Smooth navigation
   - Error recovery options

## Dependencies

- streamlit
- pandas
- requests
- collections (OrderedDict)

## Future Improvements

1. **Potential Enhancements**
   - Pin search functionality
   - Custom categories
   - Pin sharing options
   - Analytics tracking

2. **Technical Improvements**
   - Enhanced error handling
   - Performance optimizations
   - Additional caching strategies

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. (Optional) Edit or replace `pins.csv` with your own Pinterest pins. The CSV should have columns: `url`, `title`, `description`.

3. Run the app:
   ```bash
   streamlit run pint.py
   ```

4. Open the provided local URL in your browser.

## Example `pins.csv`
```
url,title,description
https://www.pinterest.com/pin/99360735500167749/,Beautiful Nature,Stunning view of a mountain landscape
https://www.pinterest.com/pin/99360735500167750/,Creative Workspace,Modern and creative office setup
https://www.pinterest.com/pin/99360735500167751/,Delicious Food,Appetizing plate of pasta
``` 