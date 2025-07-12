# app.py – Flask backend for Page Turner

# Routes:
# '/' : Homepage with genre form
# '/recommendations' : Displays scraped book recommendations

# Relies on:
# bookscraper.py for scraping book data
# templates/index.html and templates/results.html for UI


from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

# creates an instance of the flask app which is the main object that runs your website 
app = Flask(__name__)

# GENRE_URLS - this is needed to retrive the data from the website so you can interact with it 
GENRE_URLS = {
    "travel": "http://books.toscrape.com/catalogue/category/books/travel_2/index.html",
    "mystery": "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
    "historical-fiction": "http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html",
    "science-fiction": "http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html",
    "romance": "http://books.toscrape.com/catalogue/category/books/romance_8/index.html"
}

# scrape_books_by_genre (imports commented out and moved to top)
# import requests --> to handle data submitted from forms (like selected genre)
# from bs4 import BeautifulSoup --> this is a library used for web scraping 

def scrape_books_by_genre(genre_url):
    response = requests.get(genre_url)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    results = []

    for book in books:
        title = book.h3.a['title']

        # Star ratings out of 5 
        star_tag = book.find('p', class_='star-rating')
        star_class = star_tag.get('class', [])
        
        # Convert star class to a number
        rating_map = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }
        rating_text = star_class[1] if len(star_class) > 1 else "No rating"
        star_rating = rating_map.get(rating_text, 0)

        # Link to book detail page (to get author) 
        partial_url = book.h3.a['href']
        book_url = "http://books.toscrape.com/catalogue/" + partial_url.replace('../../../', '')

        # Author (from book detail page) --> function below to find the author in the book descriptions (if not found = unknown)
        author = "Unknown"
        try:
            book_response = requests.get(book_url)
            if book_response.status_code == 200:
                book_soup = BeautifulSoup(book_response.text, 'html.parser')
                rows = book_soup.find('table').find_all('tr')
                author = "Unknown"
                for row in rows:
                    header = row.find('th').text.strip()
                    if header == "Author":
                        author = row.find('td').text.strip()
                        break

        except Exception as e:
            print(f"Error fetching author: {e}")
        
        # The following information will be visible to the users 
        results.append({
            "title": title,
            "rating": star_rating,
            "author": author
        })

    return results


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    genre = request.form.get('genre')
    url = GENRE_URLS.get(genre)
    if not url:
        return "Sorry, genre not found."

    books = scrape_books_by_genre(url)
    return render_template('results.html', genre=genre.title(), books=books)

if __name__ == '__main__':
    app.run(debug=True)