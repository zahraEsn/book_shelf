from typing import List, Optional
from app.database import get_db_cursor
from app.schemas.user import User, UserUpdate
import logging

# Configure logging
logger = logging.getLogger(__name__)

def get_all_users():
    """Fetch all users from the database."""
    with get_db_cursor() as cur:
        cur.execute("SELECT * FROM users")
        return cur.fetchall()

def read_user(user_id: int):
    """Fetch a single user by its ID."""
    with get_db_cursor() as cur:
        cur.execute("SELECT * FROM books WHERE id = %s", (user_id,))
        return cur.fetchone()

def create_user(user: User):
    """Create a new user in the database."""
    with get_db_cursor() as cur:
        cur.execute(
            "INSERT INTO users (username, first_name, last_name, role, phone, email, password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (user.username, user.first_name, user.last_name, user.role, user.phone, user.email, user.password),
        )
    logger.info("user created successfully.")

def update_user(user_id: int, user: UserUpdate):
    """Update an existing user in the database."""
    with get_db_cursor() as cur:
        cur.execute(
            "UPDATE users set username = %s, first_name = %s, last_name = %s, role = %s, phone = %s, email = %s, password = %s WHERE id = %s",
            (user.username, user.first_name, user.last_name, user.role, user.phone, user.email, user.password, user_id)
        )
    logger.info("user updated successfully.")


def delete_user(user_id: int):
    """Delete a user from the database by its ID."""
    with get_db_cursor() as cur:
        cur.execute("DELETE FROM books WHERE id = %s", (user_id,))
    logger.info("Book deleted successfully.")