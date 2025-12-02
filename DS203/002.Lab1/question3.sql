CREATE VIEW customer_email_org
AS
SELECT 
    * 
FROM 
    customer_info 
WHERE 
    email 
LIKE 
    '%.org';
