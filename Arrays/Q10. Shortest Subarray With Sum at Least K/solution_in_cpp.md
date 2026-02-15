# Shortest Subarray with Sum at Least K

## Problem Statement
Given an integer array `nums` and an integer `k`, return the **length of the shortest non-empty subarray** with a sum **at least `k`**.  
If no such subarray exists, return `-1`.

---

## Intuition
This problem involves finding a **minimum-length subarray** whose sum is ≥ `k`.  
A simple sliding window does **not work** because the array can contain **negative numbers**, which breaks monotonic window expansion.

To solve this efficiently, we use:
- **Prefix Sum**
- **Monotonic Deque**

---

## Key Observations
- Let `prefix[i]` be the sum of elements from index `0` to `i-1`
- We want:
prefix[j] - prefix[i] >= k
→ Find the smallest `(j - i)`
- To minimize length, we need the **smallest index `i`** such that the condition holds

---

## Optimized Approach (Prefix Sum + Deque)

### Idea
- Use a deque to store indices of prefix sums
- Maintain the deque in **increasing order of prefix sums**
- For each index `i`:
- Check if current prefix sum minus the smallest prefix sum ≥ `k`
- If yes, update answer and pop from front
- Remove larger prefix sums from the back to keep deque optimal

---

## Algorithm
1. Compute prefix sum array
2. Initialize an empty deque
3. Traverse prefix sums:
 - While front satisfies condition → update result
 - While back has larger prefix sum → pop back
 - Push current index
4. Return result or `-1` if not found

---

## Code (C++)

```cpp
class Solution {
public:
  int shortestSubarray(vector<int>& nums, int k) {
      int n = nums.size();
      vector<long long> prefix(n + 1, 0);
      for (int i = 0; i < n; i++) {
          prefix[i + 1] = prefix[i] + nums[i];
      }

      deque<int> dq;
      int ans = n + 1;

      for (int i = 0; i <= n; i++) {
          while (!dq.empty() && prefix[i] - prefix[dq.front()] >= k) {
              ans = min(ans, i - dq.front());
              dq.pop_front();
          }

          while (!dq.empty() && prefix[i] <= prefix[dq.back()]) {
              dq.pop_back();
          }

          dq.push_back(i);
      }

      return ans == n + 1 ? -1 : ans;
  }
};
```

## Time & Space Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)
