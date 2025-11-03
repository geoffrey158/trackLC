# Last updated: 11/2/2025, 8:22:35 PM
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        longest = 0
        unique = 0 
        hashMap = {} 

        for char in s:

            hashMap[char] = hashMap.get(char,0) + 1


        for key in hashMap:
            longest = longest + (hashMap[key] - hashMap[key]%2)
            if hashMap[key]%2 == 1:
                unique = 1 
        
        
    

        return longest + unique


        

        
