# Problem 7: Delete Duplicate Emails

## Problem Statement
Write a solution to **delete** all duplicate emails, keeping only one unique email with the smallest `id`.
For SQL users, please note that you are supposed to write a `DELETE` statement and not a `SELECT` one.

**Table: Person**
| Column Name | Type |
| :--- | :--- |
| id | int |
| email | varchar |

`id` is the primary key column for this table. Each row of this table contains an email. The emails will not contain uppercase letters.

---

## Approach

This is a DML (Data Manipulation Language) problem where we modify the table.
We want to keep the row with the minimum `id` for each `email`. Therefore, any row that shares an `email` with another row but has a larger `id` should be deleted.

We can achieve this using a Self Join in the `DELETE` statement.
We alias the table as `p1` and `p2`. We join them where `p1.email = p2.email`.
We want to delete `p1` if its ID is greater than `p2`'s ID.

---

## SQL Query Solution

### MySQL Solution (Self Join)

```sql
DELETE p1
FROM Person p1
JOIN Person p2 ON p1.email = p2.email
WHERE p1.id > p2.id;
```

### Alternative Approach: Subquery (Careful with MySQL)
You might try to delete rows where the ID is not in the list of minimum IDs. However, in MySQL, you cannot modify the same table which you use in the `SELECT` part of a subquery directly. You have to wrap it in another subquery to bypass this restriction.

```sql
DELETE FROM Person
WHERE id NOT IN (
    SELECT min_id FROM (
        SELECT MIN(id) as min_id
        FROM Person
        GROUP BY email
    ) as temp_table
);
```

---

## Key Takeaways
- You can perform joins in `UPDATE` and `DELETE` statements just like you do in `SELECT` statements. This is highly efficient for modifying data based on relationships.
- Understanding the database-specific constraints (like MySQL's restriction on deleting from a table being read in a subquery) is important for real-world SQL.
