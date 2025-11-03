# Last updated: 11/2/2025, 8:23:34 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashset = set()

        for n in nums:

            if n in hashset:
                return True 
            
            hashset.add(n)

        return False 
        
