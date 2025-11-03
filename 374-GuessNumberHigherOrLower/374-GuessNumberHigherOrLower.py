# Last updated: 11/2/2025, 8:23:12 PM
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #pick number from 1 to n 

        left = 1
        right = n

        while left <= right:

            mid = left + (right-left)//2
            #use pre-defined API to return 3 possible results 
            if guess(mid) == 0:#guess is equal to the picked number
                return mid 
            elif guess(mid) == -1:#guess is greater than the picked number
                right = mid - 1 
            else: #guess is lower than the picked number
                left = mid + 1 

        #Time complexity: O(logn), binary search
        #Space complexity: O(1)