# Page Turner 📚

Page Turner is a full-stack book recommendation web app designed for fellow book lovers to discover their next great read by genre. This project integrates the Google Books API to provide real-time book data with a clean and responsive user interface.

## Features

- Genre-based search with live data from Google Books  
- Clean and responsive UI with pagination to browse results in sets of 10  
- Modular code structure with clear separation of backend logic and frontend presentation  

## Tech Stack & Tools

- Python + Flask for backend development and routing  
- Google Books API for book data (title, author, description, cover, rating)  
- Jinja2 templating engine for rendering HTML pages dynamically  
- HTML and CSS for frontend structure and styling  
- Requests library to fetch data from the Google Books API  

## Installation & Setup

1. Clone the repository:  
   ```bash
   git clone https://github.com/YOUR_USERNAME/page-turner.git
2. Navigate to the project directory:
   ```bash
   cd page-turner
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
5. Run the Flask app:
   ```bash
   python app.py
6. Open your browser and go to http://127.0.0.1:5000/ to use the app.

## Usage
- Select a book genre from the dropdown menu on the homepage.
- Browse recommended books fetched live from Google Books.
- Use the pagination buttons to navigate through results.

