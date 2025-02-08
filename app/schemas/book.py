from typing import List, Optional, Union
from pydantic import BaseModel, field_validator
import re


#book
class BookBase(BaseModel):
    ISBN: str
    authors_id: Union[List[int], int] = None
    genre_id: Optional[int] = None
    title: str
    price: float
    description: str
    units: int

    # @field_validator("ISBN")
    # @classmethod
    # def validate_isbn(cls, value: str) -> str:
    #     if not re.match(r"^\d{3}-\d{1,5}-\d{1,7}-\d{1,7}-\d{1}$", value):
    #         raise ValueError("Invalid ISBN format")
    #     return value

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    ISBN: Optional[str]

    @field_validator("ISBN")
    @classmethod
    def validate_isbn(cls, value: str) -> str:
        if not re.match(r"^\d{3}-\d{1,5}-\d{1,7}-\d{1,7}-\d{1}$", value):
            raise ValueError("Invalid ISBN format")
        return value

class Book(BookBase):
    id: Optional[int]
