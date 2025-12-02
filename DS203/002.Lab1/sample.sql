CREATE VIEW customer_city_view AS 
SELECT 
    first_name, 
    last_name, 
    email, 
    city 
FROM 
    customer 
JOIN 
    address USING (address_id) 
JOIN 
    city USING (city_id);