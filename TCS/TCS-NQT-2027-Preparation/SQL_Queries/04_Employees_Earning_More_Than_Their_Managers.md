# Problem 4: Employees Earning More Than Their Managers

## Problem Statement
Write a solution to find the employees who earn more than their managers.
Return the result table in any order.

**Table: Employee**
| Column Name | Type |
| :--- | :--- |
| id | int |
| name | varchar |
| salary | int |
| managerId | int |

`id` is the primary key column for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.

---

## Approach

We need to compare two records within the **same** table: an employee's record and their manager's record.
To do this, we must perform a **Self Join**. We join the `Employee` table to itself.
- Let one instance of the table represent the Employee (alias `e`).
- Let the other instance represent the Manager (alias `m`).

We join them on the condition that the employee's `managerId` equals the manager's `id`.
Then, we filter where the employee's `salary` > the manager's `salary`.

---

## SQL Query Solution

```sql
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;
```

### Alternative Approach: Subquery (Usually slower)
You can also solve this using a subquery in the WHERE clause, though the JOIN approach is standard and typically more optimized by the database engine.

```sql
SELECT name AS Employee
FROM Employee e
WHERE salary > (
    SELECT salary 
    FROM Employee m 
    WHERE m.id = e.managerId
);
```

---

## Key Takeaways
- **Self Joins** are crucial when comparing hierarchical data or data within the same table against itself.
- Use `AS` to rename the output column if the problem statement requests a specific column name (e.g., `AS Employee`).
