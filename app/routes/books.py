from typing import List
from fastapi import APIRouter, HTTPException, status
from psycopg2._psycopg import IntegrityError
from pydantic import ValidationError
from app.schemas.book import Book, BookCreate, BookUpdate
from app.sevices.book import get_all_books, read_book, create_book, update_book, delete_book

router = APIRouter(prefix="/books", tags=["books"])
@router.get("", response_model=List[Book])
def get_books():
    books = get_all_books()
    if books is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Books not found')
    books_list = [
        Book(
            id=book[0],
            authors_id=book[1],
            genre_id=book[2],
            title=book[3],
            ISBN=book[4],
            price=book[5],
            description=book[6],
            units=book[7]
        )
        for book in books
    ]
    return books_list

@router.get("/{book_id}", response_model=Book)
def read_book_endpoint(book_id: int):
    book = read_book(book_id)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')
    return {"id": book[0], "authors_id":book[1], "genre_id": book[2], "title":book[3], "ISBN": book[4],
            "price": book[5], "description": book[6], "units": book[7]}

@router.post("", status_code=status.HTTP_201_CREATED)
def create_book_endpoint(book: BookCreate):
    try:
        create_book(book)
        return {"message": "Book created successfully"}
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Book with this ISBN already exists,"
                                                    " or we have not this author_id or genre_id")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")


@router.put("/{book_id}", response_model=dict)
def update_book_endpoint(book_id: int, book: BookUpdate):
    try:
        update_book(book_id, book)
        return {"message": "Book updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_endpoint(book_id: int):
    book = read_book(book_id)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')
    delete_book(book_id)