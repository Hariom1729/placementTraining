# Problem 8: Rising Temperature

## Problem Statement
Write a solution to find all dates' `id` with higher temperatures compared to its previous dates (yesterday).
Return the result table in any order.

**Table: Weather**
| Column Name | Type |
| :--- | :--- |
| id | int |
| recordDate | date |
| temperature | int |

`id` is the primary key for this table.
This table contains information about the temperature on a certain day.

---

## Approach

We need to compare a row's temperature with the temperature of the row representing exactly one day prior.
Since we are comparing a table to itself based on a condition, we use a **Self Join**.

Let the tables be `w1` (representing "today") and `w2` (representing "yesterday").
We need two conditions to match "today" with its correct "yesterday":
1. `w1.temperature > w2.temperature`
2. `w1.recordDate` is exactly 1 day after `w2.recordDate`.

To compare dates, we cannot simply use `- 1` because SQL date logic handles months and leap years. We must use a built-in date difference function.
In MySQL, `DATEDIFF(date1, date2)` returns the number of days between two dates.

---

## SQL Query Solution

### MySQL Solution

```sql
SELECT w1.id
FROM Weather w1
JOIN Weather w2
-- Join condition: w1's date is exactly 1 day after w2's date
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;
```

### PostgreSQL / SQL Server Equivalent
Different dialects use different date addition/subtraction functions.
```sql
-- PostgreSQL
SELECT w1.id
FROM Weather w1
JOIN Weather w2
ON w1.recordDate = w2.recordDate + INTERVAL '1 day'
WHERE w1.temperature > w2.temperature;
```

---

## Key Takeaways
- **Never do math on raw dates** (like `date - 1`). Always use the specific date manipulation functions provided by your SQL dialect (e.g., `DATEDIFF`, `DATE_ADD`, `INTERVAL`).
- Self joins are again the perfect tool for comparing rows within the same table.
