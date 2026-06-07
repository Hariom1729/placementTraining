# SQL Interview Questions & Practical Queries

Zoho frequently tests complex SQL writing involving analytical functions, joins, and aggregations.

## 1. Basic to Medium Queries

**Q1. Find the 2nd Highest Salary.**
```sql
SELECT MAX(salary) AS SecondHighestSalary 
FROM Employee 
WHERE salary < (SELECT MAX(salary) FROM Employee);
```

**Q2. Find employees who earn more than their managers.**
```sql
SELECT E1.name 
FROM Employee E1
JOIN Employee E2 ON E1.managerId = E2.id
WHERE E1.salary > E2.salary;
```

**Q3. Delete duplicate emails keeping the one with the lowest ID.**
```sql
DELETE p1 
FROM Person p1, Person p2 
WHERE p1.email = p2.email AND p1.id > p2.id;
```

## 2. Advanced Joins & Aggregations

**Q4. Find the department with the highest average salary.**
```sql
SELECT department_name 
FROM Employees
GROUP BY department_name
ORDER BY AVG(salary) DESC
LIMIT 1;
```

**Q5. Find customers who never ordered.**
```sql
SELECT c.name 
FROM Customers c
LEFT JOIN Orders o ON c.id = o.customerId
WHERE o.id IS NULL;
```

**Q6. Display the number of employees in each department. Only include departments with more than 5 employees.**
```sql
SELECT department_id, COUNT(*) as emp_count
FROM Employees
GROUP BY department_id
HAVING COUNT(*) > 5;
```

## 3. Window Functions (Crucial for Zoho)

**Q7. Find the Nth highest salary using Window Functions.**
```sql
WITH RankedSalaries AS (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
    FROM Employee
)
SELECT salary FROM RankedSalaries WHERE rnk = N;
```
*Explanation:* `DENSE_RANK()` handles duplicates correctly without skipping ranks.

**Q8. Calculate the cumulative sum (running total) of sales per day.**
```sql
SELECT date, amount,
       SUM(amount) OVER (ORDER BY date) as running_total
FROM Sales;
```

**Q9. Find the top 3 highest paid employees in EACH department.**
```sql
WITH DeptRanks AS (
    SELECT e.name, e.salary, d.name as dept_name,
           DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) as rnk
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
)
SELECT dept_name, name, salary 
FROM DeptRanks 
WHERE rnk <= 3;
```
*Explanation:* `PARTITION BY` resets the rank counter for each new department.

## 4. Case Statements and Complex Logic

**Q10. Reformat a table from Long to Wide format (Pivot).**
Problem: Table `Revenue` has (id, month, revenue). Make columns for Jan_Rev, Feb_Rev, etc.
```sql
SELECT id,
       SUM(CASE WHEN month = 'Jan' THEN revenue ELSE 0 END) AS Jan_Rev,
       SUM(CASE WHEN month = 'Feb' THEN revenue ELSE 0 END) AS Feb_Rev,
       SUM(CASE WHEN month = 'Mar' THEN revenue ELSE 0 END) AS Mar_Rev
FROM Revenue
GROUP BY id;
```

**Q11. Swap the 'm' and 'f' values in a gender column with a single update.**
```sql
UPDATE Salary 
SET sex = CASE 
            WHEN sex = 'm' THEN 'f' 
            ELSE 'm' 
          END;
```

## 5. Theory Questions Expected in SQL Round
1. **WHERE vs HAVING:** `WHERE` filters rows before aggregation. `HAVING` filters groups after aggregation (usually used with `GROUP BY`).
2. **UNION vs UNION ALL:** `UNION` removes duplicates and is slower (requires sorting). `UNION ALL` retains duplicates and is faster.
3. **TRUNCATE vs DELETE:** `TRUNCATE` is DDL (resets identity, faster, cannot be rolled back in some DBs). `DELETE` is DML (logs each row, can trigger `ON DELETE`, can be rolled back).
4. **Execution Order of SQL:** `FROM` -> `WHERE` -> `GROUP BY` -> `HAVING` -> `SELECT` -> `ORDER BY` -> `LIMIT`.
