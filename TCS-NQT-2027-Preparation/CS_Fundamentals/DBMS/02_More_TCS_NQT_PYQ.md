# Database Management Systems - Extended TCS NQT Interview Questions (Part 2)

Advanced SQL and DBMS concepts frequently encountered.

---

## 11. What is the difference between a Primary Key and a Candidate Key?
**Answer:**
- **Candidate Key:** Any column or set of columns that can uniquely identify a row in a table. A table can have multiple candidate keys.
- **Primary Key:** The single candidate key chosen by the database designer to act as the main identifier for the table. There can only be one Primary Key per table. Every Primary Key is a Candidate Key, but not every Candidate Key is a Primary Key.

## 12. Explain the concept of Foreign Key Constraints (CASCADE, SET NULL, NO ACTION).
**Answer:**
When a row referenced by a Foreign Key is deleted or updated in the parent table, the database must decide what to do with the child rows:
- **CASCADE:** Automatically deletes or updates the corresponding child rows.
- **SET NULL:** Sets the foreign key column in the child rows to NULL.
- **NO ACTION / RESTRICT:** Rejects the delete or update operation on the parent row and throws an error, protecting referential integrity.

## 13. What is the difference between the `HAVING` clause and the `WHERE` clause?
**Answer:**
- **WHERE:** Filters individual rows *before* any grouping or aggregation takes place. Cannot be used with aggregate functions like `SUM()`, `COUNT()`.
- **HAVING:** Filters groups of rows *after* the `GROUP BY` clause has been applied and aggregations have been calculated. Used specifically with aggregate functions.

## 14. What are Database Transactions and what does `COMMIT` and `ROLLBACK` do?
**Answer:**
A transaction is a single logical unit of work consisting of one or more SQL statements (e.g., deducting money from Account A and adding it to Account B).
- **COMMIT:** Saves all changes made during the current transaction permanently to the database.
- **ROLLBACK:** Undoes all changes made during the current transaction, returning the database to the state it was in before the transaction began (used if an error occurs mid-transaction).

## 15. What is the difference between Clustered and Non-Clustered Indexes?
**Answer:**
- **Clustered Index:** Defines the physical sorting order of the data rows in the table. Because the data itself is sorted, there can be only ONE clustered index per table (usually the Primary Key). Extremely fast for range queries.
- **Non-Clustered Index:** Creates a separate structure from the data rows that contains the index key and a pointer to the actual data row. A table can have multiple non-clustered indexes.

## 16. What is a Self Join? Give a practical example.
**Answer:**
A Self Join is a regular join, but the table is joined with itself. You must use table aliases so SQL knows which instance of the table you are referring to.
**Example:** An `Employee` table where each employee has a `ManagerID` which references the `EmployeeID` of their manager in the *same* table. You use a self join to get an employee's name alongside their manager's name.

## 17. What is the difference between `UNION` and `UNION ALL`?
**Answer:**
Both operators combine the result sets of two or more `SELECT` statements into a single result set.
- **UNION:** Removes duplicate rows from the combined result set. It is slower because it has to perform a distinct operation.
- **UNION ALL:** Includes all duplicate rows. It is much faster because it simply appends the result sets together without checking for duplicates.

## 18. What is a Subquery? What are Correlated Subqueries?
**Answer:**
- **Subquery (Inner Query):** A query nested inside another query. The inner query executes first, and its result is passed to the outer query.
- **Correlated Subquery:** A subquery that uses values from the outer query. Because it depends on the outer query, it cannot be executed independently. The inner query is executed once for *every* row processed by the outer query, making it notoriously slow.

## 19. What is Entity-Relationship (ER) Modeling?
**Answer:**
ER modeling is a conceptual design process used to represent the data structures and relationships in a database system.
- **Entity:** A real-world object (e.g., Student, Course). Represents a table.
- **Attribute:** A property of the entity (e.g., StudentName, Age). Represents a column.
- **Relationship:** How entities interact with each other (e.g., Student *enrolls in* Course). Types include 1:1, 1:N, N:N.

## 20. What is Database Denormalization? Why do it?
**Answer:**
Denormalization is the process of intentionally introducing redundancy into a normalized database schema. 
While normalization optimizes for write speeds and data integrity, highly normalized databases often require complex, slow multi-table joins for read operations. Denormalization optimizes for **read speeds** by grouping frequently accessed data together, at the cost of slower writes and using more disk space.
