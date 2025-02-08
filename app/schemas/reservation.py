from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class ReservationBase(BaseModel):
    customer_id: int
    book_id: int
    start_date: datetime
    end_date: datetime
    price: float

class ReservationCreate(ReservationBase):
    pass

class ReservationUpdate(ReservationBase):
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    price: Optional[float]

class Reservation(ReservationBase):
    id: int