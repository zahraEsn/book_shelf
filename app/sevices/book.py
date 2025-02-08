from app.database import get_db_cursor
from app.schemas.book import Book, BookUpdate
import logging

logger = logging.getLogger(__name__)

def get_all_books():
    """Fetch all books from the database."""
    with get_db_cursor() as cur:
        cur.execute("SELECT * FROM books")
        return cur.fetchall()

def read_book(book_id: int):
    """Fetch a single book by its ID."""
    with get_db_cursor() as cur:
        cur.execute("SELECT * FROM books WHERE id = %s", (book_id,))
        return cur.fetchone()

def create_book(book: Book):
    """Create a new book in the database."""
    with get_db_cursor() as cur:
        cur.execute(
            "INSERT INTO books (genre_id, authors_id, title, ISBN, price, description, units) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (book.genre_id, book.authors_id, book.title, book.ISBN, book.price, book.description, book.units),
        )
    logger.info("Book created successfully.")

def update_book(book_id: int, book: BookUpdate):
    """Update an existing book in the database."""
    with get_db_cursor() as cur:
        cur.execute(
            "UPDATE books SET genre_id = %s, authors_id = %s, title = %s, ISBN = %s, price = %s, description = %s, units = %s WHERE id = %s",
            (book.genre_id, book.authors_id, book.title, book.ISBN, book.price, book.description, book.units, book_id)
        )
    logger.info("Book updated successfully.")

def delete_book(book_id: int):
    """Delete a book from the database by its ID."""
    with get_db_cursor() as cur:
        cur.execute("DELETE FROM books WHERE id = %s", (book_id,))
    logger.info("Book deleted successfully.")