# Solution: Tree Node

## Problem Summary
You are given a table `Tree` that represents a hierarchical tree structure.  
Each row contains:
- `id` → the current node
- `p_id` → the parent node (can be `NULL`)

Your task is to classify each node into one of the following types:
- **Root** → Node with no parent (`p_id IS NULL`)
- **Inner** → Node that has a parent **and** at least one child
- **Leaf** → Node that has a parent but no children

---

## SQL Solution

```sql
SELECT 
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (
            SELECT DISTINCT p_id 
            FROM Tree 
            WHERE p_id IS NOT NULL
        ) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree;
```
## Explanation

```WHEN p_id IS NULL THEN 'Root'```
- Identifies the root node of the tree.

```WHEN id IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL)```
- Checks whether the current node appears as a parent for any other node.
- If yes, it is an Inner node.

```ELSE 'Leaf'```
- Nodes that are neither root nor parent nodes are classified as Leaf nodes.
