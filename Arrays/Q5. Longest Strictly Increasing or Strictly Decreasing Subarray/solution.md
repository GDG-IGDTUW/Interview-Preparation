## Approach

We scan the array once while tracking:

- The length of the **current strictly increasing subarray**
- The length of the **current strictly decreasing subarray**
- The **maximum length** found so far

### Key Observations

- If `nums[i] > nums[i-1]`, the increasing streak continues and the decreasing streak resets.
- If `nums[i] < nums[i-1]`, the decreasing streak continues and the increasing streak resets.
- If `nums[i] == nums[i-1]`, both streaks reset to `1`.

At each step, update the maximum length.

---

## Algorithm

1. Initialize:
   - `inc = 1` (length of current increasing subarray)
   - `dec = 1` (length of current decreasing subarray)
   - `ans = 1`
2. Iterate from index `1` to `n-1`:
   - Compare `nums[i]` with `nums[i-1]`
   - Update `inc` and `dec` accordingly
   - Update `ans`
3. Return `ans`

---

## Complexity Analysis

- **Time Complexity:** `O(N)`  
  Single pass through the array.

- **Space Complexity:** `O(1)`  
  Only constant extra variables are used.

---

## C++ Implementation

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;

        int inc = 1, dec = 1, ans = 1;

        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                inc++;
                dec = 1;
            } else if (nums[i] < nums[i - 1]) {
                dec++;
                inc = 1;
            } else {
                inc = 1;
                dec = 1;
            }
            ans = max(ans, max(inc, dec));
        }

        return ans;
    }
};
```
