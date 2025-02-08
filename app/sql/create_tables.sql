CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    role VARCHAR(10) CHECK (role IN ('admin', 'customer', 'author')) NOT NULL,
    phone VARCHAR(15),
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    city_id INT NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    goodreader_link VARCHAR(255),
    bank_account_number VARCHAR(50),
    FOREIGN KEY (city_id) REFERENCES city(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    subscription_model VARCHAR(20) CHECK (subscription_model IN ('free', 'plus', 'premium')) NOT NULL,
    subscription_end_time TIMESTAMP,
    wallet_money_amount DECIMAL(10, 2) NOT NULL
);

CREATE TABLE city (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE genre (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    genre_id INT REFERENCES genre(id),
    authors_id INT[] REFERENCES authors(id) NOT NULL,
    title VARCHAR(255) NOT NULL,
    ISBN VARCHAR(20) NOT NULL UNIQUE,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    units INT NOT NULL
);

CREATE TABLE reservations (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    book_id INT REFERENCES books(id),
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);