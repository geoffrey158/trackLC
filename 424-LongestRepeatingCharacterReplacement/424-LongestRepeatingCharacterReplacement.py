# Last updated: 11/2/2025, 8:22:33 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0

        hashmap = {} 
        freq = 0
        left = 0 
        
        for right in range(len(s)):

            hashmap[s[right]] = 1 + hashmap.get(s[right],0)
            freq = max(freq, hashmap[s[right]])

            if freq + k >= (right-left+1):
                res = right-left+1 
            else:
                hashmap[s[left]] -= 1 
                left += 1 
        

        return res 