# bookapi.py
# Anushka Khurpa

import requests  # library to make HTTP requests

def get_books_by_genre(genre, start_index=0, max_results=10):
    # build the API URL using the selected genre
    url = "https://www.googleapis.com/books/v1/volumes"
    
    # prepare query parameters for the API request
    query_data = {
        'q': f"subject:{genre}",       # search books by genre
        'startIndex': start_index,     # start index for pagination
        'maxResults': max_results,     # number of books per page (max 40)
        'printType': 'books',          # only return books (not magazines, etc.)
        'langRestrict': 'en'           # filter to only English data
    }
    # send the request to the Google Books API
    response = requests.get(url, params=query_data)

    # convert the response from JSON text --> Python dictionary
    data = response.json()

    books = []  # create a list to store results
    for item in data.get('items', []):
        volume = item.get('volumeInfo', {}) # this is where all the book information resides
        # create a dictionary for each book's info like title, author, etc
        books.append({
            'title': volume.get('title', 'No title'),
            'author': ', '.join(volume.get('authors', ['Unknown'])),
            'description': volume.get('description', 'No description'),
            'rating': volume.get('averageRating', 'N/A'),
            'thumbnail': volume.get('imageLinks', {}).get('thumbnail', '')
        })

    # return the list of books and total count (used for pagination)
    return books, data.get('totalItems', 0)
