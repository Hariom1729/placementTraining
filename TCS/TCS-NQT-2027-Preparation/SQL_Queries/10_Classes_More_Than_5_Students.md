# Problem 10: Classes More Than 5 Students

## Problem Statement
Write a solution to find all the classes that have at least 5 students.
Return the result table in any order.

**Table: Courses**
| Column Name | Type |
| :--- | :--- |
| student | varchar |
| class | varchar |

`(student, class)` is the primary key column for this table.
Each row of this table indicates the name of a student and the class in which they are enrolled.

---

## Approach

We need to count the number of students in each class and only output the classes where that count is 5 or more.

1. Group the rows by `class`.
2. Count the number of students per class. We can use `COUNT(student)` for this.
3. Since we want to filter the result *after* the grouping and counting have occurred, we must use the `HAVING` clause, not the `WHERE` clause.

---

## SQL Query Solution

```sql
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;
```

*(Note: Because the primary key is `(student, class)`, we are guaranteed that a student won't be listed twice for the same class. If they could be, we would need to use `COUNT(DISTINCT student)` instead).*

---

## Key Takeaways
- **WHERE vs HAVING:** 
  - `WHERE` filters rows *before* they are grouped.
  - `HAVING` filters groups *after* the `GROUP BY` has aggregated the rows.
- If an aggregate function like `COUNT()` is part of your filtering logic, you almost certainly need a `HAVING` clause.
