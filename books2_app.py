from fastapi import FastAPI, Path, Query, HTTPException
from book import Book
from request_models import BookRequest
from starlette import status


app = FastAPI()


BOOKS = [
    Book(1, "Computer Science Pro", "codingwithroby",
         "A very nice book", 5, 2010),
    Book(2, "Be Fast with FastAPI", "coingwithroby", "A great book", 5, 2011),
    Book(3,  "Master Endpoints", "codingwithroby", "An awesome book", 5, 2012),
    Book(4, "HP!", "Author 1", "Book Description", 2, 2013),
    Book(5, "HP2", "Author 2", "Book Description", 3, 2014),
    Book(6, "HP3", "Author 3", "Book Description", 1, 2015)
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    new_book = find_book_id(new_book)
    BOOKS.append(new_book)


def find_book_id(book: Book):
    if len(BOOKS) > 1:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    return book


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found.")


@app.get("/books/")
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found.")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found.")


@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_books_by_published_date(published_date: int = Query(gt=1999, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return
