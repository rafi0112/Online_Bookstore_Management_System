books = []

def add_book(title, author,genre,price):
    book = {"title": title,
            "author": author, 
            "genre": genre, 
            "price":price}
    books.append(book)

def list_books():
    return books
