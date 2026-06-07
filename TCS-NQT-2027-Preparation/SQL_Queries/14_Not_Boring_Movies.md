# Problem 14: Not Boring Movies

## Problem Statement
Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".
Return the result table ordered by `rating` in descending order.

**Table: Cinema**
| Column Name | Type |
| :--- | :--- |
| id | int |
| movie | varchar |
| description | varchar |
| rating | float |

`id` is the primary key for this table. Each row contains information about the name of a movie, its genre, and its rating.

---

## Approach

This is a simple filtering and sorting problem.
We need two conditions in our `WHERE` clause:
1. `id` is odd. In SQL, the modulo operator is `%` or `MOD()`. So, `id % 2 != 0` or `MOD(id, 2) = 1`.
2. `description` is not "boring". We use the inequality operator `<>` or `!=`. So, `description != 'boring'`.

Finally, we need to sort the result by `rating` in descending order using `ORDER BY rating DESC`.

---

## SQL Query Solution

```sql
SELECT 
    id, 
    movie, 
    description, 
    rating
FROM 
    Cinema
WHERE 
    id % 2 != 0 
    AND description != 'boring'
ORDER BY 
    rating DESC;
```

---

## Key Takeaways
- The modulo operator `%` works in SQL just like in C++/Java. It is extremely useful for identifying odd/even rows.
- Inequality in SQL can be written as `!=` or `<>`. `!=` is more common for programmers coming from C++/Java, while `<>` is the traditional SQL standard. Both work in almost all modern databases.
