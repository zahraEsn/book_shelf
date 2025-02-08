INSERT INTO books (genre_id, authors_id, title, ISBN, price, genre, description, units)
VALUES (1, 1, 'The Quantum Paradox', '978-3-16-148410-0', 25.99, 'Science Fiction',
'A mind-bending journey into the mysteries of quantum physics.', 50);

INSERT INTO users (username, first_name, last_name, role, phone, email, password)
VALUES ('bookworm99', 'Mark', 'Lee', 'customer',
'+1 555-5678', 'mark.lee@example.com	', '	R34dM0r3!');

INSERT INTO authors (user_id, city_id, first_name, last_name, goodreader_link, bank_account_number)
VALUES (2, 1, 'Daniel', 'Mitchell',
'https://www.goodreads.com/user/show/12345678-daniel-mitchell', '3481 7623 9856 2147');

INSERT INTO city (id, name) VALUES (7, 'boshehr')
INSERT INTO genre (id, name) VALUES (7, 'thriller')

INSERT INTO customers (user_id, subscription_model, subscription_end_time, wallet_money_amount)
VALUES (2, 'free', '2025-06-30 14:57:12', 50.45);

INSERT INTO books (genre_id, authors_id, title, ISBN, price, genre, description, units)
VALUES (null, null,'The Quantum Paradox', '978-3-16-148410-0', 25.99, 'Science',
        'A mind-bending journey into the mysteries of quantum physics.', 50);