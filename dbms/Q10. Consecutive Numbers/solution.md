# Consecutive Numbers 

**Problem:**
Find all numbers that appear at least three times consecutively in the Logs table.
Table Structure:
- id – continuous, increasing
- num – integer

**Solution 1: Self-Join (Sliding Window via Joins)**

**Idea**

Create a sliding window of 3 consecutive rows using self-joins on id.
If all three rows contain the same num, it is a valid result.

**SQL Query**
```sql
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.id = l2.id - 1
JOIN Logs l3 ON l2.id = l3.id - 1
WHERE l1.num = l2.num
  AND l2.num = l3.num;
```
**✔ Why It Works**

- Ensures rows are consecutive using id
- Checks equality across three adjacent rows
- DISTINCT removes duplicates
- No false positives

**Solution 2: Using LAG() Window Function**

**Idea**

Compare the current row’s value with the previous two rows using LAG().

**SQL Query**
```sql
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT 
        num,
        LAG(num, 1) OVER (ORDER BY id) AS prev1,
        LAG(num, 2) OVER (ORDER BY id) AS prev2
    FROM Logs
) t
WHERE num = prev1
  AND num = prev2;
```
**Why It Works**

- LAG(num, 1) → previous row
- LAG(num, 2) → two rows before
- Ensures three consecutive rows have the same value
- Cleaner and more readable than self-joins

**Bonus: Sliding Window Logic Explained**

Both solutions use a window size of 3:

- Window = [row i-2, row i-1, row i]
- Condition: num[i] = num[i-1] = num[i-2]
- Self-Join approach: manually shifts the window using id
- LAG approach: shifts the window logically using window functions
