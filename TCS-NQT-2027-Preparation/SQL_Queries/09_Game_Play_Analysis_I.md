# Problem 9: Game Play Analysis I

## Problem Statement
Write a solution to report the first login date for each player.
Return the result table in any order.

**Table: Activity**
| Column Name | Type |
| :--- | :--- |
| player_id | int |
| device_id | int |
| event_date | date |
| games_played | int |

`(player_id, event_date)` is the primary key of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.

---

## Approach

This is a classic and very straightforward aggregation problem.
We need to find the earliest (minimum) `event_date` for each unique `player_id`.

To do this, we:
1. Group the table by `player_id`.
2. Select the `player_id`.
3. Select the minimum `event_date` using the `MIN()` aggregate function.

---

## SQL Query Solution

```sql
SELECT 
    player_id, 
    MIN(event_date) AS first_login
FROM 
    Activity
GROUP BY 
    player_id;
```

---

## Key Takeaways
- Aggregate functions like `MIN()`, `MAX()`, `SUM()`, `AVG()` are almost always paired with a `GROUP BY` clause.
- When you use `GROUP BY`, every column in your `SELECT` statement MUST either be in the `GROUP BY` clause or be wrapped in an aggregate function.
