from typing import List
from fastapi import APIRouter, HTTPException, status
from psycopg2._psycopg import IntegrityError
from pydantic import ValidationError
from app.schemas.reservation import Reservation, ReservationCreate, ReservationUpdate
from app.sevices.reservation import get_all_reservations, read_reservation, create_reservation, update_reservation, delete_reservation

router = APIRouter(prefix="/reservations", tags=["reservations"])
@router.get("", response_model=List[Reservation])
def get_reservations():
    reservations = get_all_reservations()
    if reservations is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Reservations not found')
    reservations_list = [
        Reservation(
            id=reservation[0],
            customer_id=reservation[1],
            book_id=reservation[2],
            start_date=reservation[3],
            end_date=reservation[4],
            price=reservation[5]
        )
        for reservation in reservations
    ]
    return reservations_list

@router.get("/{reservation_id}", response_model=Reservation)
def read_reservation_endpoint(reservation_id: int):
    reservation = read_reservation(reservation_id)
    if reservation is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Reservation not found')
    return {"id": reservation[0], "customer_id":reservation[1], "book_id": reservation[2],
            "start_date":reservation[3], "end_date": reservation[4], "price": reservation[5]}

@router.post("", status_code=status.HTTP_201_CREATED)
def create_reservation_endpoint(reservation: ReservationCreate):
    try:
        create_reservation(reservation)
        return {"message": "Reservation created successfully"}
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Reservation with this email or username already exists")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")


@router.put("/{reservation_id}", response_model=dict)
def update_reservation_endpoint(reservation_id: int, reservation: ReservationUpdate):
    try:
        update_reservation(reservation_id, reservation)
        return {"message": "Reservation updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{reservation_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reservation_endpoint(reservation_id: int):
    reservation = read_reservation(reservation_id)
    if reservation is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Reservation not found')
    delete_reservation(reservation_id)