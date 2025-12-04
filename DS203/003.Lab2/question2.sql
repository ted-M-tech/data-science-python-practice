-- Query 1: Before dropping the index
EXPLAIN ANALYZE SELECT * FROM customer WHERE email = 'some.email@example.com';

-- Query 2: Drop the index
DROP INDEX idx_customer_email;

-- Query 3: After dropping the index
EXPLAIN ANALYZE SELECT * FROM customer WHERE email = 'some.email@example.com';