# Problem 5: Customers Who Never Order

## Problem Statement
Write a solution to find all customers who never order anything.
Return the result table in any order.

**Table: Customers**
| Column Name | Type |
| :--- | :--- |
| id | int |
| name | varchar |

`id` is the primary key column for this table.

**Table: Orders**
| Column Name | Type |
| :--- | :--- |
| id | int |
| customerId | int |

`id` is the primary key column for this table. `customerId` is a foreign key of the ID from the Customers table.

---

## Approach 1: LEFT JOIN with NULL Check

We want to find records in the `Customers` table that do NOT have a corresponding record in the `Orders` table.
If we do a `LEFT JOIN` from `Customers` to `Orders`, customers with no orders will have `NULL` values in the `Orders` columns.
We can then simply filter for those `NULL`s.

## Approach 2: NOT IN / NOT EXISTS Subquery

We can select all customer names whose `id` is NOT present in the list of `customerId`s from the `Orders` table.

---

## SQL Query Solutions

### Solution 1: LEFT JOIN (Generally the most efficient)

```sql
SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o ON c.id = o.customerId
WHERE o.id IS NULL;
```

### Solution 2: NOT IN

```sql
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId FROM Orders
);
```

### Solution 3: NOT EXISTS

```sql
SELECT c.name AS Customers
FROM Customers c
WHERE NOT EXISTS (
    SELECT 1 
    FROM Orders o 
    WHERE o.customerId = c.id
);
```

---

## Key Takeaways
- Finding "missing" relationships between two tables is a classic SQL pattern.
- `LEFT JOIN ... WHERE right_table.id IS NULL` is the standard "Anti-Join" pattern.
- `NOT IN` is very readable but can behave unexpectedly if the subquery returns any `NULL` values. `NOT EXISTS` is generally safer and faster for large datasets.
