# Last updated: 11/2/2025, 8:22:12 PM
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #Binary search over possible ship capacities.

        left = max(weights) #Edge Case: Smallest possible capacity (must carry heaviest item)
        right = sum(weights) #Largest possible capacity (carry all at once)
        res = right # Store the minimum valid capacity found

        while left <= right:
            mid = left + (right-left)//2 

            dayCount = 1 #Starts with day 1,keeps track of the number of days it takes to ship all the packages
            currWeight = 0 #Keeps track of the current weight on the ship 
            for w in weights:
                #Exceeds today's capacity, ship current load and start next day
                if currWeight + w > mid:
                    dayCount += 1
                    currWeight = 0
                currWeight += w #Add the weight of each new package 

            #current ship weight is valid, now check for a lower weight capacity answer
            if dayCount <= days:
                res = mid                
                right = mid - 1
            else: #current ship weight is not valid, weight has to be higher to be a valid answer
                left = mid + 1
        
        return res
            
        #Time complexity: O(nlogs) 
        #O(n) is the loop to check shipping all the packages for each mid value
        #O(logs) is the binary search over the range of possible capacities to binary search over
        
        #Space complexity: O(1)