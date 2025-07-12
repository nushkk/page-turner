import requests
from bs4 import BeautifulSoup

def scrape_books_by_genre(genre_url):
    response = requests.get(genre_url)
    if response.status_code != 200:
        print("Failed to retrieve page")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all book titles on the page
    books = soup.find_all('article', class_='product_pod')
    titles = [book.h3.a['title'] for book in books]

    return titles

if __name__ == "__main__":
    # Example genre URL (Travel)
    travel_url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
    books = scrape_books_by_genre(travel_url)
    print("Books in Travel genre:")
    for title in books:
        print("-", title)