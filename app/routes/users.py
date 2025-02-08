from typing import List
from fastapi import APIRouter, HTTPException, status
from psycopg2._psycopg import IntegrityError
from pydantic import ValidationError
from app.schemas.user import User, UserCreate, UserUpdate
from app.sevices.user import get_all_users, read_user, create_user, update_user, delete_user

router = APIRouter(prefix="/users", tags=["users"])
@router.get("", response_model=List[User])
def get_users():
    users = get_all_users()
    if users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Users not found')
    users_list = [
        User(
            id=user[0],
            username=user[1],
            first_name=user[2],
            last_name=user[3],
            role=user[4],
            phone=user[5],
            email=user[6]
        )
        for user in users
    ]
    return users_list

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = read_user(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return {"id":user[0], "username": user[1], "first_name": user[2], "last_name": user[3], "role": user[4],
            "phone": user[5], "email": user[6]}

@router.post("", status_code=status.HTTP_201_CREATED)
def create_user_endpoint(user: UserCreate):
    try:
        create_user(user)
        return {"message": "User created successfully"}
    except IntegrityError:
        raise HTTPException(status_code=400, detail="User with this email or username already exists")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")


@router.put("/{user_id}", response_model=dict)
def update_user_endpoint(user_id: int, user: UserUpdate):
    try:
        update_user(user_id, user)
        return {"message": "User updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_endpoint(user_id: int):
    user = read_user(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    delete_user(user_id)