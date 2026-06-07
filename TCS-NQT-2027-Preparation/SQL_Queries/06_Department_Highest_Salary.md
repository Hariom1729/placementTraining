# Problem 6: Department Highest Salary

## Problem Statement
Write a solution to find employees who have the highest salary in each of the departments.
Return the result table in any order.

**Table: Employee**
| Column Name | Type |
| :--- | :--- |
| id | int |
| name | varchar |
| salary | int |
| departmentId | int |

`id` is the primary key column for this table. `departmentId` is a foreign key of the ID from the Department table.

**Table: Department**
| Column Name | Type |
| :--- | :--- |
| id | int |
| name | varchar |

`id` is the primary key column for this table.

---

## Approach 1: Subquery with IN clause

We can find the maximum salary for each department by grouping the `Employee` table by `departmentId`.
Then, we query the `Employee` table again, joined with the `Department` table, and filter for rows where the `(departmentId, salary)` pair exists in the result of our subquery.

## Approach 2: Window Functions (Modern SQL)

We can use the `RANK()` or `DENSE_RANK()` window function, partitioning by `departmentId` and ordering by `salary DESC`. Then we simply select the rows where the rank is 1.

---

## SQL Query Solutions

### Solution 1: Using IN clause with multiple columns (Standard SQL)

```sql
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM 
    Employee e
JOIN 
    Department d ON e.departmentId = d.id
WHERE 
    (e.departmentId, e.salary) IN (
        SELECT departmentId, MAX(salary)
        FROM Employee
        GROUP BY departmentId
    );
```

### Solution 2: Using Window Functions (More efficient and scalable)

```sql
WITH RankedSalaries AS (
    SELECT 
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER(PARTITION BY e.departmentId ORDER BY e.salary DESC) as rnk
    FROM 
        Employee e
    JOIN 
        Department d ON e.departmentId = d.id
)
SELECT 
    Department, 
    Employee, 
    Salary
FROM 
    RankedSalaries
WHERE 
    rnk = 1;
```

---

## Key Takeaways
- You can use the `IN` operator to match multiple columns simultaneously `(col1, col2) IN (SELECT col1, col2 ...)`.
- Using Common Table Expressions (`WITH` clause) makes complex queries using window functions much more readable.
