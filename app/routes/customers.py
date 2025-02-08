from typing import List
from fastapi import APIRouter, HTTPException, status
from psycopg2._psycopg import IntegrityError
from pydantic import ValidationError
from app.schemas.customer import Customer, CustomerCreate, CustomerUpdate
from app.sevices.customer import get_all_customers, read_customer, create_customer, update_customer, delete_customer

router = APIRouter(prefix="/customers", tags=["customers"])
@router.get("", response_model=List[Customer])
def get_customers():
    customers = get_all_customers()
    if customers is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Customer not found')
    customers_list = [
        Customer(
            id=customer[0],
            user_id=customer[1],
            subscription_model=customer[2],
            subscription_end_time=customer[3],
            wallet_money_amount=customer[4]
        )
        for customer in customers
    ]
    return customers_list

@router.get("/{customer_id}", response_model=Customer)
def get_customer(customer_id: int):
    customer = read_customer(customer_id)
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Customer not found')
    return {"id":customer[0], "user_id": customer[1], "subscription_model": customer[2], "subscription_end_time": customer[3],
            "wallet_money_amount": customer[4]}

@router.post("", status_code=status.HTTP_201_CREATED)
def create_customer_endpoint(customer: CustomerCreate):
    try:
        create_customer(customer)
        return {"message": "Customer created successfully"}
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Customer with this user_id already exists or this user_id doesn't exist")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

@router.put("/{customer_id}", response_model=dict)
def update_customer_endpoint(customer_id: int, customer: CustomerUpdate):
    try:
        update_customer(customer_id, customer)
        return {"message": "Customer updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_endpoint(customer_id: int):
    customer = read_customer(customer_id)
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Customer not found')
    delete_customer(customer_id)