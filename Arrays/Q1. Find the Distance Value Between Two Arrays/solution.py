from bisect import bisect_left

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        """
        APPROACH:
        We need to count how many elements x in arr1 are such that
        for EVERY element y in arr2:
                |x - y| > d
        
        Instead of comparing x with all elements in arr2 (O(n*m)),
        we optimize using sorting + binary search.

        Steps:
        1. Sort arr2.
        2. For each element x in arr1:
           - Use binary search to find where x would be inserted in arr2.
           - Only the closest neighbours can violate the condition:
                • element just before insertion index
                • element at insertion index
           - If neither is within distance d, x is valid.
        3. Count such valid elements.

        WHY THIS WORKS:
        In a sorted array, the closest value to x must lie near its
        insertion position. No need to check the entire array.

        TIME COMPLEXITY:
        Sorting arr2 → O(m log m)
        For each element in arr1 → binary search O(log m)
        Total → O(m log m + n log m)

        SPACE COMPLEXITY:
        O(1) auxiliary space (ignoring sort internal space)
        """

        # Sort arr2 to allow binary search
        arr2.sort()
        
        count = 0  # number of valid elements in arr1
        
        # Check each element in arr1
        for x in arr1:
            
            # Position where x would be inserted in sorted arr2
            pos = bisect_left(arr2, x)
            
            # Assume x is valid initially
            valid = True
            
            # Check closest smaller element (left neighbour)
            if pos > 0 and abs(x - arr2[pos - 1]) <= d:
                valid = False
            
            # Check closest greater/equal element (right neighbour)
            if pos < len(arr2) and abs(arr2[pos] - x) <= d:
                valid = False
            
            # If no element in arr2 is within distance d
            if valid:
                count += 1
        
        return count
