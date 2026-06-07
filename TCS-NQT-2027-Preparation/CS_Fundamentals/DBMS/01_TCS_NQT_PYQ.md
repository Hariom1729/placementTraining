# Database Management Systems (DBMS) - TCS NQT Last 5 Years PYQs

DBMS is heavily tested in TCS interviews, alongside SQL queries.

---

## 1. What are ACID properties in a Database?
**Answer:**
ACID ensures database transactions are processed reliably:
- **Atomicity:** "All or nothing". Either the entire transaction succeeds, or the entire transaction fails and is rolled back. No partial updates.
- **Consistency:** The database must remain in a valid state before and after the transaction, following all defined rules and constraints.
- **Isolation:** Concurrent transactions execute independently without interfering with each other.
- **Durability:** Once a transaction is committed, it remains committed permanently, even in the event of a system crash or power failure.

## 2. Explain the different types of Normalization (1NF, 2NF, 3NF, BCNF).
**Answer:**
Normalization is the process of organizing data to reduce redundancy and improve data integrity.
- **1NF (First Normal Form):** Every column must contain atomic (indivisible) values. No repeating groups or arrays.
- **2NF:** Must be in 1NF, and all non-key attributes must be fully functionally dependent on the Primary Key. (No partial dependency).
- **3NF:** Must be in 2NF, and there should be no transitive dependency (non-key attributes should not depend on other non-key attributes).
- **BCNF (Boyce-Codd Normal Form):** A stricter version of 3NF. For every functional dependency X -> Y, X must be a super key.

## 3. What is the difference between Primary Key, Unique Key, and Foreign Key?
**Answer:**
- **Primary Key:** Uniquely identifies each record. Cannot contain NULL values. Only one per table.
- **Unique Key:** Uniquely identifies records, but can accept exactly ONE NULL value. A table can have multiple unique keys.
- **Foreign Key:** A field in one table that uniquely identifies a row of another table (or the same table). It creates a relationship between two tables and ensures referential integrity.

## 4. Differentiate between DELETE, TRUNCATE, and DROP.
**Answer:**
- **DELETE:** A DML command. Removes specific rows based on a WHERE condition. Can be rolled back. Slower, as it logs each deleted row.
- **TRUNCATE:** A DDL command. Removes ALL rows from a table instantly, leaving the table structure intact. Cannot be rolled back in most DBs. Faster.
- **DROP:** A DDL command. Completely deletes the table data AND the table structure from the database. Cannot be rolled back.

## 5. What are the different types of Joins?
**Answer:**
- **INNER JOIN:** Returns records that have matching values in both tables.
- **LEFT (OUTER) JOIN:** Returns all records from the left table, and the matched records from the right table. Fills with NULL if no match.
- **RIGHT (OUTER) JOIN:** Returns all records from the right table, and the matched records from the left table.
- **FULL (OUTER) JOIN:** Returns all records when there is a match in either the left or right table.
- **CROSS JOIN:** Returns the Cartesian product of the two tables.

## 6. What is an Index? How does it improve performance?
**Answer:**
An index is a database data structure (usually a B-Tree or Hash Table) that improves the speed of data retrieval operations on a database table. It acts like an index in a book. Instead of scanning every row in a massive table (Full Table Scan), the DB engine uses the index to quickly locate the data. However, indexes slow down write operations (INSERT, UPDATE) because the index must also be updated.

## 7. What is a View?
**Answer:**
A View is a virtual table based on the result-set of an SQL statement. It contains rows and columns, just like a real table, but it doesn't store data itself. It provides a security layer (hiding complex queries or sensitive columns from users) and simplifies query execution.

## 8. What is the difference between DDL, DML, DCL, and TCL?
**Answer:**
- **DDL (Data Definition Language):** Defines structure. CREATE, ALTER, DROP, TRUNCATE.
- **DML (Data Manipulation Language):** Manipulates data. SELECT, INSERT, UPDATE, DELETE.
- **DCL (Data Control Language):** Controls access. GRANT, REVOKE.
- **TCL (Transaction Control Language):** Manages transactions. COMMIT, ROLLBACK, SAVEPOINT.

## 9. What is a Stored Procedure?
**Answer:**
A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again. It is compiled and stored in the database. It reduces network traffic (only the call is sent over the network, not the huge query) and improves security (prevents SQL injection).

## 10. What is a Trigger?
**Answer:**
A Trigger is a special type of stored procedure that automatically executes (fires) in response to certain events on a particular table or view in a database (e.g., BEFORE INSERT, AFTER UPDATE). It is often used to enforce business rules or maintain audit logs.
