from fastapi import FastAPI


app = FastAPI()


BOOKS = [
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'category': 'fiction'},
    {'title': 'A Brief History of Time',
        'author': 'Stephen Hawking', 'category': 'science'},
    {'title': '1984', 'author': 'George Orwell', 'category': 'fiction'},
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
