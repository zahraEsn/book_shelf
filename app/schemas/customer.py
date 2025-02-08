from typing import Optional, Literal
from pydantic import BaseModel
from datetime import datetime

class CustomerBase(BaseModel):
    subscription_model: Literal["free", "plus", "premium"]
    subscription_end_time: Optional[datetime] = None
    wallet_money_amount: float

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    subscription_end_time: Optional[datetime]
    wallet_money_amount: Optional[int]

class Customer(CustomerBase):
    user_id: Optional[int]
    id: Optional[int]
