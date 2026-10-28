from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "title": "Дюна",
        "author": "Фрэнк Герберт",
        "genre": "Научная фантастика"
    },
    {
        "title": "Марсианин",
        "author": "Энди Вейер",
        "genre": "Научная фантастика"
    },
    {
        "title": "Основание",
        "author": "Айзек Азимов",
        "genre": "Научная фантастика"
    }
]

@app.get("/")
def read_root():
    return {
        "service": "API библиотеки фантастики",
        "path": "/books"
    }

@app.get("/books")
def get_books():
    return books