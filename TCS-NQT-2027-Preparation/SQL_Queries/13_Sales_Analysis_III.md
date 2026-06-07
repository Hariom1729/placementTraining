# Problem 13: Sales Analysis III

## Problem Statement
Write a solution to report the products that were **only** sold in the first quarter of 2019. That is, between `2019-01-01` and `2019-03-31` inclusive.
Return the result table in any order.

**Table: Product**
| Column Name | Type |
| :--- | :--- |
| product_id | int |
| product_name | varchar |
| unit_price | int |

`product_id` is the primary key of this table.

**Table: Sales**
| Column Name | Type |
| :--- | :--- |
| seller_id | int |
| product_id | int |
| buyer_id | int |
| sale_date | date |
| quantity | int |
| price | int |

This table can have duplicate rows. `product_id` is a foreign key to the Product table.

---

## Approach

We need to find products where ALL of their sales occurred within the specified date range. If a product has even one sale outside this range, it should be excluded.

We can solve this by finding the minimum and maximum sale dates for each product.
If the minimum sale date is `>= '2019-01-01'` AND the maximum sale date is `<= '2019-03-31'`, then we know for a fact that all sales for that product fell within that quarter.

1. Group the `Sales` table by `product_id`.
2. Use `HAVING` to check `MIN(sale_date)` and `MAX(sale_date)`.
3. Join with the `Product` table to get the `product_name`.

---

## SQL Query Solution

```sql
SELECT 
    p.product_id, 
    p.product_name
FROM 
    Product p
JOIN 
    Sales s ON p.product_id = s.product_id
GROUP BY 
    p.product_id, 
    p.product_name
HAVING 
    MIN(s.sale_date) >= '2019-01-01' 
    AND MAX(s.sale_date) <= '2019-03-31';
```

### Alternative Approach (Subqueries)

Find all products sold outside the quarter, and then exclude them.

```sql
SELECT product_id, product_name
FROM Product
WHERE product_id IN (SELECT product_id FROM Sales WHERE sale_date BETWEEN '2019-01-01' AND '2019-03-31')
  AND product_id NOT IN (SELECT product_id FROM Sales WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31');
```
*(The GROUP BY / HAVING approach is generally preferred as it is cleaner and often more performant than multiple subqueries).*

---

## Key Takeaways
- Using `MIN()` and `MAX()` on dates inside a `HAVING` clause is a powerful technique for determining if a group of records completely falls within a specific time window.
