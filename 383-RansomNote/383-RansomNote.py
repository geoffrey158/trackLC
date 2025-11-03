# Last updated: 11/2/2025, 8:23:12 PM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        hashMap = {}

        for c in magazine:
            hashMap[c] = hashMap.get(c,0) + 1

        for c in ransomNote:
            if hashMap.get(c) == None or hashMap.get(c) <= 0:
                return False

            hashMap[c] = hashMap.get(c) - 1
        
        return True 

