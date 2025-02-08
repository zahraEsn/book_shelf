from typing import List, Optional
from app.database import get_db_cursor
from app.schemas.customer import Customer, CustomerUpdate
import logging

# Configure logging
logger = logging.getLogger(__name__)

def get_all_customers() -> List[tuple]:
    """Fetch all customers from the database."""
    with get_db_cursor() as cur:
        cur.execute("SELECT * FROM customers")
        return cur.fetchall()

def read_customer(customer_id: int) -> Optional[tuple]:
    """Fetch a single customer by their ID."""
    with get_db_cursor() as cur:
        cur.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
        return cur.fetchone()

def create_customer(customer: Customer) -> None:
    """Create a new customer in the database."""
    with get_db_cursor() as cur:
        cur.execute(
            "INSERT INTO customers (user_id, subscription_model, subscription_end_time, wallet_money_amount) VALUES (%s, %s, %s, %s)",
            (customer.user_id, customer.subscription_model, customer.subscription_end_time, customer.wallet_money_amount),
        )
    logger.info("Customer created successfully.")

def update_customer(customer_id: int, customer: CustomerUpdate) -> None:
    """Update an existing customer in the database."""
    with get_db_cursor() as cur:
        cur.execute(
            "UPDATE customers SET user_id = %s, subscription_model = %s, subscription_end_time = %s, wallet_money_amount = %s WHERE id = %s",
            (customer.user_id, customer.subscription_model, customer.subscription_end_time, customer.wallet_money_amount, customer_id),
        )
    logger.info("Customer updated successfully.")

def delete_customer(customer_id: int) -> None:
    """Delete a customer from the database by their ID."""
    with get_db_cursor() as cur:
        cur.execute("DELETE FROM customers WHERE id = %s", (customer_id,))
    logger.info("Customer deleted successfully.")