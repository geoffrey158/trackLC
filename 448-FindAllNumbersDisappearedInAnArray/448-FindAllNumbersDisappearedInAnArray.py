# Last updated: 11/2/2025, 8:22:30 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        #Mark as seen by negation 
        res = [] 
        for c in nums:
            nums[abs(c)-1] = -abs(nums[abs(c)-1]) #mark as negative for numbers that have been seen 
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1) #all the non negative numbers have not been seen 
        return res

        """
        Time Complexity : O(n), we only iterate nums twice each taking O(n) time at most.
        Space Complexity : O(1), only constant extra space is being used except for the output ans.
        """