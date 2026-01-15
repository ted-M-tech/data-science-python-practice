-- Question 1: Create a function to categorize films by length.
-- This function takes a film_id, finds the film's length, and returns
-- 'Short', 'Medium', or 'Long' based on the length.
CREATE OR REPLACE FUNCTION get_film_length_category(p_film_id INT)
RETURNS TEXT AS $$
DECLARE
    v_length INT;
    v_category TEXT;
BEGIN
    -- Get the length of the film from the film table
    SELECT length INTO v_length FROM film WHERE film_id = p_film_id;

    IF v_length < 60 THEN
        v_category := 'Short';
    ELSIF v_length BETWEEN 60 AND 120 THEN
        v_category := 'Medium';
    ELSE
        v_category := 'Long';
    END IF;

    RETURN v_category;
END;
$$ LANGUAGE plpgsql;

-- Usage example for Q1:
SELECT get_film_length_category(1); -- Example for a specific film_id


-- Question 2: Create a function to get the status of a customer.
-- This function takes a customer_id and returns 'Active', 'Inactive', or 'New'
-- based on the number of films they have rented.
CREATE OR REPLACE FUNCTION get_customer_status(p_customer_id INT)
RETURNS TEXT AS $$
DECLARE
    v_rental_count INT;
    v_status TEXT;
BEGIN
    -- Count the number of rentals for the given customer
    SELECT COUNT(*) INTO v_rental_count FROM rental WHERE customer_id = p_customer_id;

    -- Determine the customer's status
    IF v_rental_count > 5 THEN
        v_status := 'Active';
    ELSIF v_rental_count BETWEEN 1 AND 5 THEN
        v_status := 'Inactive';
    ELSE
        v_status := 'New';
    END IF;

    RETURN v_status;
END;
$$ LANGUAGE plpgsql;

-- Usage example for Q2:
SELECT get_customer_status(1); -- Example for a specific customer_id


-- Question 3: Create a function to get a customer's full name.
-- This function takes a customer_id and returns the full name by
-- concatenating first_name and last_name.
CREATE OR REPLACE FUNCTION get_customer_full_name(p_customer_id INT)
RETURNS TEXT AS $$
DECLARE
    v_full_name TEXT;
BEGIN
    -- Get the customer's full name
    SELECT first_name || ' ' || last_name INTO v_full_name FROM customer WHERE customer_id = p_customer_id;

    RETURN v_full_name;
END;
$$ LANGUAGE plpgsql;

-- Usage example for Q3:
SELECT get_customer_full_name(1); -- Example for a specific customer_id


-- Question 4: Create a stored procedure to print long films.
-- This procedure takes a minimum length and prints the titles and lengths
-- of all films that are at least that long.
CREATE OR REPLACE PROCEDURE print_long_films(min_length INT)
AS $$
DECLARE
    v_film RECORD;
BEGIN
    -- Loop through films that meet the minimum length requirement
    FOR v_film IN SELECT title, length FROM film WHERE length >= min_length LOOP
        -- Raise a notice for each film
        RAISE NOTICE 'Title: %, Length: %', v_film.title, v_film.length;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- Usage example for Q4:
CALL print_long_films(180); -- Example with a minimum length of 180 minutes


-- Question 5: Create a procedure to show inventory by category.
-- This procedure loops through each film category and prints the category name
-- along with the count of inventory items available in that category.
CREATE OR REPLACE PROCEDURE show_inventory_by_category()
AS $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN
        SELECT
            c.name AS category_name,
            COUNT(i.inventory_id) AS inventory_count
        FROM
            category AS c
        JOIN
            film_category AS fc ON c.category_id = fc.category_id
        JOIN
            inventory i ON fc.film_id = i.film_id
        GROUP BY
            c.name
        ORDER BY
            c.name
    LOOP
        RAISE NOTICE 'Category: %, Inventory Count: %', r.category_name, r.inventory_count;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- Usage example for Q5:
CALL show_inventory_by_category();
