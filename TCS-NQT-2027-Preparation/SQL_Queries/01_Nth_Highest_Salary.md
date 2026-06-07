# Problem 1: Nth Highest Salary

## Problem Statement
Write an SQL query to report the `n`th highest salary from the `Employee` table. If there is no `n`th highest salary, the query should report `null`.

**Table: Employee**
| Column Name | Type |
| :--- | :--- |
| id | int |
| salary | int |

`id` is the primary key column for this table.

---

## Approach 1: LIMIT and OFFSET (MySQL / PostgreSQL)
If `N` is fixed (e.g., finding the 2nd highest salary), we can order by salary descending, and then skip `N-1` rows and take `1`.
For the 2nd highest: `ORDER BY salary DESC LIMIT 1 OFFSET 1`.
Since `N` is a variable here, we use a SQL Function structure.

## Approach 2: Window Functions (DENSE_RANK) - Modern SQL
`DENSE_RANK()` assigns a rank to every row within a partition of a result set, with no gaps in ranking values. This handles duplicate salaries perfectly.

---

## SQL Query Solutions

### MySQL Solution (Using LIMIT/OFFSET inside a Function)

```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  -- OFFSET cannot accept mathematical expressions like N-1 directly, 
  -- so we declare a variable
  DECLARE M INT;
  SET M = N - 1;
  
  RETURN (
      SELECT DISTINCT salary 
      FROM Employee 
      ORDER BY salary DESC 
      LIMIT 1 OFFSET M
  );
END
```

### Generic SQL (Using DENSE_RANK)
*(If the question just asks for a specific N, like 2nd highest)*

```sql
-- Finding the 2nd highest salary
SELECT MAX(salary) AS SecondHighestSalary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rank_num
    FROM Employee
) AS ranked_salaries
WHERE rank_num = 2;
```

---

## Key Takeaways
- `DISTINCT` is necessary because two employees might have the same top salary.
- `LIMIT N OFFSET M` is heavily used in pagination logic.
- `DENSE_RANK()` is mathematically cleaner when dealing with duplicate values compared to standard `RANK()` which leaves gaps (e.g., ranks 1, 1, 3 instead of 1, 1, 2).
