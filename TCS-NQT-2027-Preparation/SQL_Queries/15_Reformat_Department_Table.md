# Problem 15: Reformat Department Table

## Problem Statement
Write an SQL query to reformat the table such that there is a department id column and a revenue column for each month.
Return the result table in any order.

**Table: Department**
| Column Name | Type |
| :--- | :--- |
| id | int |
| revenue | int |
| month | varchar |

`(id, month)` is the primary key of this table.
The table has information about the revenue of each department per month. The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].

---

## Approach: Pivoting Table

This is a classic "Pivot" operation where we turn rows into columns.
Since there's a fixed number of months (12), we can manually write out the columns.

We want one row per `id`. So we will `GROUP BY id`.
For the monthly revenue columns, we want to extract the revenue only if the row corresponds to that specific month. We can use the `CASE` statement inside an aggregate function like `SUM()` or `MAX()` to achieve this.

For example, for the `Jan` column: `SUM(CASE WHEN month = 'Jan' THEN revenue ELSE null END) AS Jan_Revenue`.
If a department doesn't have revenue for January, the `SUM` of nulls will evaluate to `null`, which perfectly satisfies the requirement.

---

## SQL Query Solution

```sql
SELECT 
    id,
    SUM(CASE WHEN month = 'Jan' THEN revenue ELSE null END) AS Jan_Revenue,
    SUM(CASE WHEN month = 'Feb' THEN revenue ELSE null END) AS Feb_Revenue,
    SUM(CASE WHEN month = 'Mar' THEN revenue ELSE null END) AS Mar_Revenue,
    SUM(CASE WHEN month = 'Apr' THEN revenue ELSE null END) AS Apr_Revenue,
    SUM(CASE WHEN month = 'May' THEN revenue ELSE null END) AS May_Revenue,
    SUM(CASE WHEN month = 'Jun' THEN revenue ELSE null END) AS Jun_Revenue,
    SUM(CASE WHEN month = 'Jul' THEN revenue ELSE null END) AS Jul_Revenue,
    SUM(CASE WHEN month = 'Aug' THEN revenue ELSE null END) AS Aug_Revenue,
    SUM(CASE WHEN month = 'Sep' THEN revenue ELSE null END) AS Sep_Revenue,
    SUM(CASE WHEN month = 'Oct' THEN revenue ELSE null END) AS Oct_Revenue,
    SUM(CASE WHEN month = 'Nov' THEN revenue ELSE null END) AS Nov_Revenue,
    SUM(CASE WHEN month = 'Dec' THEN revenue ELSE null END) AS Dec_Revenue
FROM 
    Department
GROUP BY 
    id;
```

---

## Key Takeaways
- Combining `SUM()` (or `MAX()`) with a `CASE` statement is the standard SQL way to perform a Pivot operation when a dedicated `PIVOT` operator isn't available or required.
- The `ELSE null` is technically optional (since `CASE` defaults to `NULL` if no condition matches), but writing it explicitly improves readability.
