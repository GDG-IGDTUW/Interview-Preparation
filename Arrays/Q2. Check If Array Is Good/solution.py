"""
Problem: Check If Array Is Good

Intuition:
-----------
A "good" array of length n must contain exactly:
    [1, 2, 3, ..., n-1, n-1]

Meaning:
- Numbers from 1 to n-1 must appear exactly once
- The number (n-1) must appear twice
- No other number should appear
- Length of array must be n

So the array should look like:
set(nums) == {1,2,3,...,n-1}
AND
frequency of (n-1) == 2
AND
all other numbers appear exactly once

Example:
[1,2,3,3] -> good (n=4 → need {1,2,3} with 3 twice)

Approach:
-----------
1. Let n = length of nums
2. Valid numbers must be from 1 to n-1
3. Use frequency counting
4. Check:
    - Every number is in range [1, n-1]
    - Count of (n-1) == 2
    - Count of all others == 1

Complexity:
-----------
Time  : O(n)
Space : O(n)  (for frequency count)
"""

from collections import Counter

class Solution:
    def isGood(self, nums):
        n = len(nums)
        freq = Counter(nums)

        # Step 1: All numbers must be within range [1, n-1]
        for num in nums:
            if num < 1 or num > n-1:
                return False

        # Step 2: Check required frequencies
        for i in range(1, n):
            if i == n-1:
                if freq[i] != 2:
                    return False
            else:
                if freq[i] != 1:
                    return False

        return True
