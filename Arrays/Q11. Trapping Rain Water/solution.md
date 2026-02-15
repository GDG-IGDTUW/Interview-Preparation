# Trapping Rain Water

## Problem Statement
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

---

## Intuition
Water can be trapped **between two taller bars**.  
For any index `i`, the amount of water stored depends on:

- The **maximum height to its left**
- The **maximum height to its right**

The water trapped at index `i` is:

water[i] = min(maxLeft, maxRight) - height[i]


If `height[i]` is greater than or equal to both sides, no water is trapped.

---

## Optimized Approach (Two Pointers)

### Key Idea
Instead of precomputing left and right maximum arrays, we use **two pointers** to achieve **O(1) space**.

- Start with two pointers: `left = 0`, `right = n - 1`
- Maintain:
  - `leftMax` → maximum height from the left
  - `rightMax` → maximum height from the right
- Always move the pointer with the **smaller height**, because water level is limited by the smaller side.

---

## Algorithm
1. Initialize:
   - `left = 0`, `right = n - 1`
   - `leftMax = 0`, `rightMax = 0`
   - `water = 0`
2. While `left < right`:
   - If `height[left] <= height[right]`:
     - Update `leftMax`
     - Add trapped water at `left`
     - Move `left` forward
   - Else:
     - Update `rightMax`
     - Add trapped water at `right`
     - Move `right` backward
3. Return total trapped water

---

## Code (C++)

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int leftMax = 0, rightMax = 0;
        int water = 0;

        while (left < right) {
            if (height[left] <= height[right]) {
                leftMax = max(leftMax, height[left]);
                water += leftMax - height[left];
                left++;
            } else {
                rightMax = max(rightMax, height[right]);
                water += rightMax - height[right];
                right--;
            }
        }
        return water;
    }
};
```

## Time & Space Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)
