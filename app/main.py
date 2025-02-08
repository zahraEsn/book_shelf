from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import books, customers, reservations, users
from . import auth
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(customers.router)
app.include_router(books.router)
app.include_router(reservations.router)


@app.get("/")
def print_hello():
    return {"message": "hello, welcome to book shelf"}