# Database Management Systems (DBMS)

## 1. Architecture and Basics
**1. What is DBMS?**
Software used to store, retrieve, and manage data efficiently and securely while maintaining data integrity.

**2. Difference between RDBMS and NoSQL?**
- **RDBMS (SQL):** Relational, structured data (tables), predefined schema, scales vertically, ACID compliant (e.g., MySQL, PostgreSQL).
- **NoSQL:** Non-relational, unstructured/semi-structured data (JSON docs, key-value), dynamic schema, scales horizontally, BASE compliant (e.g., MongoDB, Redis).

## 2. Keys and Relationships
**3. Define Primary Key, Foreign Key, Candidate Key, and Super Key.**
- **Super Key:** A set of attributes that uniquely identifies a row.
- **Candidate Key:** A minimal Super Key (no redundant attributes).
- **Primary Key:** A Candidate Key selected by the database designer to uniquely identify records. Cannot be NULL.
- **Foreign Key:** An attribute that creates a link between two tables, referencing the Primary Key of another table.

## 3. Normalization
**4. What is Normalization?**
The process of organizing data to reduce redundancy and improve data integrity.
- **1NF:** Atomic values only. No repeating groups.
- **2NF:** 1NF + No partial dependency (all non-key attributes must depend on the whole primary key).
- **3NF:** 2NF + No transitive dependency (non-key attributes cannot depend on other non-key attributes).
- **BCNF:** A stricter 3NF where for every dependency $X \rightarrow Y$, $X$ must be a super key.

**5. Denormalization?**
Intentionally adding redundant data to tables to speed up complex read queries (at the cost of slower writes).

## 4. Transactions & ACID Properties
**6. What are the ACID properties?**
- **Atomicity:** All operations in a transaction succeed, or none do ("All or nothing").
- **Consistency:** The database moves from one valid state to another.
- **Isolation:** Concurrent transactions do not interfere with each other.
- **Durability:** Once committed, data is permanently saved, even in case of a system crash.

**7. Write-Ahead Logging (WAL)?**
A technique used to ensure Durability. Changes are logged to disk before the actual database pages are updated.

## 5. Concurrency Control
**8. Deadlock in DBMS?**
Occurs when two or more transactions are waiting indefinitely for one another to release locks. Resolved via timeout mechanisms or deadlock detection algorithms (Wait-for graphs).

**9. Types of Locks?**
- **Shared Lock (S):** Allows reading. Multiple transactions can hold an S lock.
- **Exclusive Lock (X):** Allows reading and writing. Only one transaction can hold an X lock.

## 6. Indexing
**10. What is Indexing?**
A data structure technique to quickly locate and access data without scanning every row (Table Scan). Usually implemented using B-Trees or B+ Trees.

**11. Clustered vs Non-Clustered Index?**
- **Clustered:** Determines the physical order of data in a table. Only 1 allowed per table (usually the Primary Key).
- **Non-Clustered:** Stores a logical order (pointers to the actual data). Multiple allowed per table.

## 7. Joins & Views
**12. Types of Joins?**
- **INNER JOIN:** Returns matching rows in both tables.
- **LEFT JOIN:** Returns all rows from the left table, and matched rows from the right.
- **RIGHT JOIN:** Returns all rows from the right table, and matched rows from the left.
- **FULL OUTER JOIN:** Returns all rows when there is a match in either table.
- **CROSS JOIN:** Cartesian product.

**13. What is a View?**
A virtual table based on the result-set of an SQL statement. Used to simplify complex queries and restrict data access for security.

## 8. Stored Procedures and Triggers
**14. Stored Procedure vs Function?**
Stored procedures can execute DML (Insert, Update) and don't necessarily return a value. Functions must return a value and cannot modify the database state.

**15. What is a Trigger?**
A stored program executed automatically to respond to a specific event (e.g., BEFORE INSERT, AFTER UPDATE) on a table.
