# Last updated: 11/2/2025, 8:23:22 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False #if the strings aren't the same size, can't be an anagram

        #hashmap for each string
        hashmapS = {} 
        hashmapT = {} 
        
        #can use s or t, since we know now it is the same length
        for i in range(len(s)):
            hashmapS[s[i]] = 1 + hashmapS.get(s[i],0)
            hashmapT[t[i]] = 1 + hashmapT.get(t[i],0)
        
        #check if the hashmaps are the same
        #if they are that means it's an anagram and returns true, false otherwise
        return hashmapS == hashmapT

        #Time Complexity:O(n + m),n is the length of string s and m is the length of string t
        #Space Complexity:O(1), since we have at most 26 different characters.
            