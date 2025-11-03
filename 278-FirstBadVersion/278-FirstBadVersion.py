# Last updated: 11/2/2025, 8:23:17 PM
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #find the first bad element

        l = 0 
        r = n

        while l < r:
            m = l + (r - l)//2 #avoid overflow 

            if isBadVersion(m) == True:
                r = m
            else: #isBadVersion(m) == False
                l = m + 1 
            

        return l