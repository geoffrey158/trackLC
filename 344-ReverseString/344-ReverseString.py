# Last updated: 11/2/2025, 8:23:13 PM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1 
            right -= 1 

        #time complexity: O(n), iterate through list once
        #space complexity: O(1)