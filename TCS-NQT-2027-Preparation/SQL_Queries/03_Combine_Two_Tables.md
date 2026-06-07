# Problem 3: Combine Two Tables

## Problem Statement
Write a solution to report the first name, last name, city, and state of each person in the `Person` table. If the address of a `personId` is not present in the `Address` table, report `null` instead.
Return the result table in any order.

**Table: Person**
| Column Name | Type |
| :--- | :--- |
| personId | int |
| lastName | varchar |
| firstName | varchar |

`personId` is the primary key column for this table.

**Table: Address**
| Column Name | Type |
| :--- | :--- |
| addressId | int |
| personId | int |
| city | varchar |
| state | varchar |

`addressId` is the primary key column for this table.

---

## Approach

The problem asks for information from both the `Person` table and the `Address` table. This indicates we need a **JOIN**.
Crucially, the problem states: "If the address of a personId is not present in the Address table, report null instead."
This means we want ALL records from the `Person` table, regardless of whether there is a matching record in the `Address` table.
An `INNER JOIN` would drop people without addresses.
Therefore, we must use a **LEFT JOIN** (or LEFT OUTER JOIN), starting with the `Person` table on the left.

---

## SQL Query Solution

```sql
SELECT 
    p.firstName, 
    p.lastName, 
    a.city, 
    a.state
FROM 
    Person p
LEFT JOIN 
    Address a 
ON 
    p.personId = a.personId;
```

---

## Key Takeaways
- **LEFT JOIN** returns all rows from the left table (`Person`), and the matched rows from the right table (`Address`). The result is `NULL` from the right side if there is no match.
- Always use table aliases (`p`, `a`) when querying multiple tables to make the query cleaner and avoid column name ambiguity if both tables have a column with the exact same name.
