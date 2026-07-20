CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    status VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS notifications (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    message TEXT NOT NULL
);

INSERT INTO users (name, email)
VALUES
('John Doe', 'john@example.com'),
('Alice Smith', 'alice@example.com');

INSERT INTO products (name, price)
VALUES
('Laptop', 65000.00),
('Wireless Mouse', 1200.00);

INSERT INTO orders (user_id, product_id, status)
VALUES
(1, 1, 'Delivered'),
(2, 2, 'Processing');

INSERT INTO notifications (user_id, message)
VALUES
(1, 'Your order has been delivered.'),
(2, 'Your order is being processed.');