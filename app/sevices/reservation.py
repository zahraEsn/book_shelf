from typing import List, Optional
from app.database import get_db_cursor
from app.schemas.reservation import Reservation, ReservationUpdate
import logging

# Configure logging
logger = logging.getLogger(__name__)

def get_all_reservations() -> List[tuple]:
    """Fetch all reservations from the database."""
    with get_db_cursor() as cur:
        cur.execute("SELECT * FROM reservations")
        return cur.fetchall()

def read_reservation(reservation_id: int) -> Optional[tuple]:
    """Fetch a single reservation by its ID."""
    with get_db_cursor() as cur:
        cur.execute("SELECT * FROM reservations WHERE id = %s", (reservation_id,))
        return cur.fetchone()

def create_reservation(reservation: Reservation) -> None:
    """Create a new reservation in the database."""
    with get_db_cursor() as cur:
        cur.execute(
            "INSERT INTO reservations (customer_id, book_id, start_date, end_date, price) VALUES (%s, %s, %s, %s, %s)",
            (reservation.customer_id, reservation.book_id, reservation.start_date, reservation.end_date, reservation.price),
        )
    logger.info("Reservation created successfully.")

def update_reservation(reservation_id: int, reservation: ReservationUpdate) -> None:
    """Update an existing reservation in the database."""
    with get_db_cursor() as cur:
        cur.execute(
            "UPDATE reservations SET customer_id = %s, book_id = %s, start_date = %s, end_date = %s, price = %s WHERE id = %s",
            (reservation.customer_id, reservation.book_id, reservation.start_date, reservation.end_date, reservation.price, reservation_id),
        )
    logger.info("Reservation updated successfully.")

def delete_reservation(reservation_id: int) -> None:
    """Delete a reservation from the database by its ID."""
    with get_db_cursor() as cur:
        cur.execute("DELETE FROM reservations WHERE id = %s", (reservation_id,))
    logger.info("Reservation deleted successfully.")