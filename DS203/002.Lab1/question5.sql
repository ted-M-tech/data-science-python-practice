DROP VIEW customer_info CASCADE;
CREATE VIEW customer_info 
AS 
SELECT 
    (first_name || ' ' || last_name) AS full_name, 
    email 
FROM 
    customer;