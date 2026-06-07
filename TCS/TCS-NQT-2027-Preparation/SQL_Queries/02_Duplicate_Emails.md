# Problem 2: Duplicate Emails

## Problem Statement
Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.
Return the result table in any order.

**Table: Person**
| Column Name | Type |
| :--- | :--- |
| id | int |
| email | varchar |

`id` is the primary key column for this table. Each row of this table contains an email.

---

## Approach

A duplicate email is an email that appears more than once in the table. We need to count the occurrences of each email and filter out the ones that appear only once.

This requires:
1. **Grouping** the rows by `email` (`GROUP BY email`).
2. **Filtering** the groups based on a condition (`HAVING COUNT(email) > 1`).

---

## SQL Query Solution

```sql
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
```

### Alternative Approach: Self Join (Less Efficient)
You can also find duplicates by joining the table to itself on the email column where the IDs are different.

```sql
SELECT DISTINCT p1.email
FROM Person p1
JOIN Person p2 ON p1.email = p2.email
WHERE p1.id != p2.id;
```

---

## Key Takeaways
- The `HAVING` clause was added to SQL because the `WHERE` keyword cannot be used with aggregate functions. 
- Always use `GROUP BY` when you want to apply an aggregate function (`COUNT`, `SUM`, `AVG`) across subsets of data.
