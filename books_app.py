from fastapi import FastAPI, Body


app = FastAPI()


BOOKS = [
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'category': 'fiction'},
    {'title': 'A Brief History of Time',
        'author': 'Stephen Hawking', 'category': 'science'},
    {'title': '1984', 'author': 'George Orwell', 'category': 'real'},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'category': 'fiction'},
    {'title': 'The Origin of Species',
        'author': 'Charles Darwin', 'category': 'science'},
    {'title': 'Sapiens: A Brief History of Humankind',
        'author': 'Yuval Noah Harari', 'category': 'history'},
    {'title': 'The Art of War', 'author': 'Sun Tzu', 'category': 'history'},
    {'title': 'A Mathematician’s Apology',
        'author': 'G.H. Hardy', 'category': 'math'},
    {'title': 'Thinking, Fast and Slow',
        'author': 'Daniel Kahneman', 'category': 'science'},
    {'title': 'The Man Who Knew Infinity',
        'author': 'Robert Kanigel', 'category': 'math'}
]


@app.get("/")
async def first_api():
    return {
        "message": "Hello Kuldeep !"
    }


@app.get("/books")
def get_all_books():
    return BOOKS

# fastapi follows chronological order
# @app.get("/books/mybook")
# async def read_all_books():
#     return {"book_title": "my_favourite_book"}


@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get("title", "").casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category", "").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author", "").casefold() == book_author.casefold() and \
                book.get("category", "").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title", "").casefold() == updated_book.get("title", "").casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title", "").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


@app.get("/books/byauthor/{book_author}")
async def get_all_books_of_category_of_author(book_author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author", "").casefold() == book_author.casefold():
            books_to_return.append(book)
    return books_to_return
