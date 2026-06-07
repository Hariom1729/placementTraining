# SQL Queries & Relational Databases

## 1. Theory & Core Concepts

Structured Query Language (SQL) is the standard language for relational database management systems (RDBMS). For technical interviews like TCS NQT, you must be comfortable writing queries that filter, aggregate, and join data across multiple tables.

### Types of SQL Commands:
1. **DDL (Data Definition Language):** `CREATE`, `ALTER`, `DROP`, `TRUNCATE`
2. **DML (Data Manipulation Language):** `INSERT`, `UPDATE`, `DELETE`
3. **DQL (Data Query Language):** `SELECT`
4. **DCL (Data Control Language):** `GRANT`, `REVOKE`
5. **TCL (Transaction Control Language):** `COMMIT`, `ROLLBACK`

### Key SQL Clauses & Order of Execution:
1. `FROM` / `JOIN` (Choose tables and how they link)
2. `WHERE` (Filter rows before aggregation)
3. `GROUP BY` (Group rows by a column)
4. `HAVING` (Filter groups after aggregation)
5. `SELECT` (Select the columns to output)
6. `ORDER BY` (Sort the output)
7. `LIMIT` / `OFFSET` (Paginate the output)

### Types of Joins:
- **INNER JOIN:** Returns records that have matching values in both tables.
- **LEFT (OUTER) JOIN:** Returns all records from the left table, and matched records from the right table. NULL if no match.
- **RIGHT (OUTER) JOIN:** Returns all records from the right table, and matched records from the left table. NULL if no match.
- **FULL (OUTER) JOIN:** Returns all records when there is a match in either left or right table.

### Important Functions & Keywords:
- **Aggregate Functions:** `COUNT()`, `SUM()`, `AVG()`, `MAX()`, `MIN()`
- **String Functions:** `CONCAT()`, `UPPER()`, `LOWER()`, `SUBSTRING()`, `LENGTH()`
- **Date Functions:** `NOW()`, `DATE_ADD()`, `DATEDIFF()`
- **Window Functions (Advanced):** `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()` (Crucial for "Nth highest" type questions).
- **Other:** `DISTINCT`, `IN`, `BETWEEN`, `LIKE` (Pattern matching), `IS NULL`.

---

## 2. Problem List
*(High frequency problems for TCS NQT)*
*   `01_Nth_Highest_Salary.md`
*   `02_Duplicate_Emails.md`
*   `03_Combine_Two_Tables.md`
*   `04_Employees_Earning_More_Than_Their_Managers.md`
*   `05_Customers_Who_Never_Order.md`
*   *(... and more)*
