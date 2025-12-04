-- Question 5: Try indexing a column with few unique values like “active” column in “customers”
-- table and compare the performance - does it help? Explain your answer.

-- Answer:

-- Indexing a column with low cardinality (few unique values) like the 'active' column 
-- in the 'customer' table is generally not recommended and often does not improve performance. 
-- In some cases, it might even degrade performance.

-- Here's why:

-- 1. High Selectivity is Key: Indexes are most effective when they have high selectivity, 
--    meaning the values in the indexed column are mostly unique. This allows the database 
--    to quickly narrow down the number of rows to retrieve. When a column has low cardinality, 
--    like a boolean 'active' column (with possible values of 'true' or 'false'), the index 
--    doesn't filter out a significant portion of the table.

-- 2. Index Overhead: Creating and maintaining an index has overhead. Every time a row is 
--    inserted, updated, or deleted, the index needs to be updated as well. For a 
--    low-cardinality index, the cost of maintaining the index might outweigh the benefits.

-- 3. Query Planner's Choice: The database's query planner is usually smart enough to 
--    recognize that using an index on a low-cardinality column is inefficient. It will 
--    likely opt for a full table scan instead, making the index unused.

-- In summary, while you can create an index on the 'active' column, it's unlikely to 
-- help performance and may even have a negative impact. It's better to focus on indexing 
-- columns with high cardinality that are frequently used in `WHERE` clauses.
