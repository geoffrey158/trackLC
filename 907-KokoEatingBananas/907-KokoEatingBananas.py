# Last updated: 11/2/2025, 8:22:19 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1  
        right = max(piles)
        res = right

        while left <= right:
            mid = left + (right-left)//2

            #see how many hours it takes to finish all the bananas at the current eating speed 
            totalTime = 0 
            for p in piles:
                totalTime += math.ceil(p/mid)
            
            #valid eating speed, see if there is a faster possible eating speed 
            if totalTime <= h:
                res = mid
                right = mid - 1  
            #not valid eating speed,eating too slow 
            else: #totalTime > h
                left = mid + 1

        return res 
            