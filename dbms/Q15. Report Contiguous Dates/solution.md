# Report Contiguous Dates – Solution

**Platform:** LeetCode  
**Problem:** Report Contiguous Dates  
**Difficulty:** Hard  
**Tags:** SQL, Window Functions, Date  
**Reference:** https://leetcode.com/problems/report-contiguous-dates/

---

##  Problem Summary

You are given a table that records dates along with their status (for example: `succeeded` or `failed`).  
The task is to **group consecutive dates having the same status** into continuous date ranges and report:

- `status`
- `start_date`
- `end_date`

The solution must:
- Correctly detect contiguous (back-to-back) dates
- Break ranges when there is a gap in dates
- Produce accurate start and end dates for each range

---

##  Core Concept: Gap-and-Island Problem

This problem is a classic **gap-and-island** problem.

- **Island:** a group of consecutive rows that belong together  
- **Gap:** a break that separates one group from another  

We solve this by:
1. Assigning row numbers ordered by date
2. Subtracting the row number from the date  
3. Rows with the same result belong to the same “island”

---

##  SQL Approach (Using Window Functions)

### Step-by-step Logic

1. Use `ROW_NUMBER()` partitioned by `status` and ordered by `date`
2. Subtract the row number from the date
3. This calculated value stays constant for contiguous dates
4. Group by `status` and the calculated value
5. Use `MIN(date)` and `MAX(date)` to get ranges

---

##  SQL Solution

```sql
WITH grouped_dates AS (
    SELECT
        status,
        date,
        DATE_SUB(date, INTERVAL 
            ROW_NUMBER() OVER (PARTITION BY status ORDER BY date) DAY
        ) AS grp
    FROM Tasks
)
SELECT
    status,
    MIN(date) AS start_date,
    MAX(date) AS end_date
FROM grouped_dates
GROUP BY status, grp
ORDER BY start_date;
```

## Time & Space Complexity
- Time Complexity: O(n log n) (due to ordering)
- Space Complexity: O(n) (CTE and window function storage)
