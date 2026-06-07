# Problem 11: User Activity for the Past 30 Days I

## Problem Statement
Write a solution to find the daily active user count for a period of 30 days ending `2019-07-27` inclusive. A user was active on someday if they made at least one activity on that day.
Return the result table in any order.

**Table: Activity**
| Column Name | Type |
| :--- | :--- |
| user_id | int |
| session_id | int |
| activity_date | date |
| activity_type | enum |

This table may have duplicate rows. The `activity_type` column is an ENUM (category) of type ('open_session', 'end_session', 'scroll_down', 'send_message').
The table shows the user activities for a social media website.

---

## Approach

We need to count the number of *distinct* users who performed *any* activity on each specific date within a given time frame.

1. **Filtering:** We only care about dates between `2019-06-28` and `2019-07-27`. We can use the `BETWEEN` operator or `DATE_ADD()` / `DATE_SUB()` depending on the SQL dialect. The simplest is often `activity_date BETWEEN '2019-06-28' AND '2019-07-27'`, or in MySQL `activity_date > DATE_SUB('2019-07-27', INTERVAL 30 DAY) AND activity_date <= '2019-07-27'`.
2. **Grouping:** We want the count *per day*, so we `GROUP BY activity_date`.
3. **Aggregation:** We need the number of *unique* active users. We use `COUNT(DISTINCT user_id)`. If a user logged in 5 times on the same day, they should only count as 1 active user for that day.

---

## SQL Query Solution

### MySQL Solution

```sql
SELECT 
    activity_date AS day, 
    COUNT(DISTINCT user_id) AS active_users
FROM 
    Activity
WHERE 
    -- Filtering for the 30 day period ending on 2019-07-27
    activity_date > DATE_SUB('2019-07-27', INTERVAL 30 DAY) 
    AND activity_date <= '2019-07-27'
GROUP BY 
    activity_date;
```

### Simpler Filtering (If Date Math Isn't Required)

```sql
SELECT 
    activity_date AS day, 
    COUNT(DISTINCT user_id) AS active_users
FROM 
    Activity
WHERE 
    activity_date BETWEEN '2019-06-28' AND '2019-07-27'
GROUP BY 
    activity_date;
```

---

## Key Takeaways
- Use `COUNT(DISTINCT column_name)` when you need to count unique occurrences within a group.
- Pay close attention to date boundaries in SQL problems (e.g., "past 30 days" usually means `date > Target - 30` and `date <= Target`, which spans exactly 30 days).
