-- Question1
CREATE INDEX idx_customer_email ON customer(email);

-- Question2
-- Query 1: Before dropping the index
EXPLAIN ANALYZE SELECT * FROM customer WHERE email = 'some.email@example.com';

-- Query 2: Drop the index
DROP INDEX idx_customer_email;

-- Query 3: After dropping the index
EXPLAIN ANALYZE SELECT * FROM customer WHERE email = 'some.email@example.com';

-- Question3
CREATE INDEX idx_actor_first_last_name ON actor(first_name, last_name);

-- Question4
SELECT * FROM pg_indexes WHERE tablename = 'actor';