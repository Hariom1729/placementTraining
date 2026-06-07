# Problem 12: Article Views I

## Problem Statement
Write a solution to find all the authors that viewed at least one of their own articles.
Return the result table sorted by `id` in ascending order.

**Table: Views**
| Column Name | Type |
| :--- | :--- |
| article_id | int |
| author_id | int |
| viewer_id | int |
| view_date | date |

There is no primary key for this table, it may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date.
Note that equal `author_id` and `viewer_id` indicate the same person.

---

## Approach

An author views their own article if the `author_id` is the same as the `viewer_id` in the same row.
We need to:
1. Filter the rows where `author_id = viewer_id`.
2. Extract the `author_id`.
3. Since an author might view their own article multiple times (or view multiple of their own articles), we need to ensure the output list contains unique authors. We use the `DISTINCT` keyword.
4. Finally, sort the result by the author's ID in ascending order using `ORDER BY`.

---

## SQL Query Solution

```sql
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id ASC;
```

---

## Key Takeaways
- The `DISTINCT` keyword is crucial when you only want a unique list of items from a table that might contain duplicates.
- Basic column comparisons (`col1 = col2`) in the `WHERE` clause are very fast.
- `ORDER BY column ASC` (Ascending) is the default, but it's good practice to write it out explicitly for clarity.
