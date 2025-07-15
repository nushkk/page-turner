# app.py – Flask backend for Page Turner (now using Google Books API instead of scraping)

from flask import Flask, render_template, request
from bookapi import get_books_by_genre  # import the function from bookapi.py

app = Flask(__name__)  # create Flask app instance

# homepage route: shows the form to select a genre
@app.route('/')
def home():
    return render_template('index.html')

# recommendations route: handles the form submission & shows results
@app.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    genre = request.values.get('genre')  
    start_index = int(request.values.get('start', 0))  # page index, default = 0, start_index tells google books API where to start listing books (Ex: Page 1 would be 0, Page 2 would be 10, Page 3 would be 20)
    # so each page would have 10 book recs each 
    # check to make sure that the user entered a genre from the menu
    if not genre:
        return "Please select a genre."

    # get books and total number of items per page from Google Books API
    books, total_items = get_books_by_genre(genre, start_index=start_index)

    # calculate if there's a next page
    next_index = start_index + 10           # Google API returns 10 results per page 
    has_more = next_index < total_items     # checks if there are more results
    prev_index = max(0, start_index - 10)   # avoids going to negative index
    current_page = start_index // 10 + 1    # calculates the current page 

    # this basically renders results page with books & pagination data from above 
    return render_template(
        'results.html',
        genre = genre.title(),
        books = books,
        start_index = start_index,
        next_index = next_index if has_more else None,
        prev_index = prev_index,
        current_page = current_page
    )

# run the website
if __name__ == '__main__':
    app.run(debug=True)