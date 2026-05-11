
CREATE TABLE sales (
    order_id INT PRIMARY KEY,
    customer_id VARCHAR(50),
    product VARCHAR(100),
    region VARCHAR(50),
    amount DECIMAL(10,2),
    order_date DATE
);
