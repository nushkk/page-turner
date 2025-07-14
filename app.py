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
    start_index = int(request.values.get('start', 0))  # page index, default = 0
    if not genre:
        return "Please select a genre."

    # get books and total number of items per page from Google Books API
    books, total_items = get_books_by_genre(genre, start_index=start_index)

    # calculate if there's a next page
    next_index = start_index + 10
    has_more = next_index < total_items

    return render_template(
        'results.html',
        genre=genre.title(),
        books=books,
        start_index=start_index,
        next_index=next_index if has_more else None
    )

# run the website
if __name__ == '__main__':
    app.run(debug=True)