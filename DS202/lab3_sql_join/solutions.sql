-- Exercise 1: Simple Subquery
SELECT *
FROM books
WHERE price > (SELECT AVG(price) FROM books);

-- Exercise 2: IN Subquery
SELECT title
FROM books
WHERE author IN (SELECT author FROM books GROUP BY author HAVING COUNT(*) > 2);

-- Exercise 3: NOT IN Subquery
SELECT title
FROM books
WHERE book_id NOT IN (SELECT book_id FROM sales);

-- Exercise 4: Subquery with Aggregation
SELECT author
FROM books
GROUP BY author
HAVING AVG(rating) > (SELECT AVG(rating) FROM books);

-- Exercise 5: Subquery with Comparison Operator
SELECT *
FROM books
WHERE price > (SELECT AVG(price) FROM books);

-- Exercise 6: Nested Subquery
SELECT *
FROM books
WHERE price > (
    SELECT AVG(price)
    FROM books
    WHERE author IN (
        SELECT author
        FROM books
        GROUP BY author
        HAVING COUNT(*) = 1
    )
);

-- Exercise 7: Subquery with Date Condition
SELECT DISTINCT b.title
FROM books b
JOIN sales s ON b.book_id = s.book_id
WHERE s.sale_date > (
    SELECT s.sale_date
    FROM sales s
    JOIN books b ON s.book_id = b.book_id
    ORDER BY b.price DESC
    LIMIT 1
);

-- Exercise 8: Correlated Subquery
SELECT b.title, s1.quantity
FROM books b
JOIN sales s1 ON b.book_id = s1.book_id
WHERE s1.sale_date = (
    SELECT MAX(s2.sale_date)
    FROM sales s2
    WHERE s2.book_id = s1.book_id
);

-- Exercise 9: EXISTS Subquery
SELECT DISTINCT b.author
FROM books b
WHERE EXISTS (
    SELECT 1
    FROM sales s
    WHERE s.book_id = b.book_id
);

-- Exercise 10: NOT EXISTS Subquery
SELECT DISTINCT author
FROM books b
WHERE NOT EXISTS (
    SELECT *
    FROM sales s
    WHERE s.book_id = b.book_id
);
