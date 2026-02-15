## 183. Customers Who Never Order

### Intuition

We need customers who **do NOT appear** in the `Orders` table.

So essentially:

Customers - Customers who ordered

This is a classic **anti-join** problem.

---

###  Approach

Use a `LEFT JOIN`:

- Join `Customers` with `Orders`
- Customers with no orders will have `NULL` in Orders side
- Filter those rows

---

###  SQL Solution

```sql
SELECT name AS Customers
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.customerId IS NULL;
```

---

###  Complexity

Time: O(N + M)  
Space: O(1)

(N = Customers, M = Orders)

---

### Alternative (NOT IN)

```sql
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId FROM Orders
);
```

---

### Best Practice

Prefer `LEFT JOIN + NULL check`

Because `NOT IN` can break if NULL values exist in subquery.
