# Last updated: 11/2/2025, 8:22:13 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = "" #return string that is word1 and word2 merged
        w1 = len(word1) #length of word1
        w2 = len(word2) #length of word2

        #use the word that has the longer length as the range 
        for i in range(max(w1,w2)):
            #if there are any remaining letters in word1 add to merged
            if i < w1:
                merged += word1[i]
        
            #if there are any remaining letters in word2 add to merged
            if i < w2:
                merged += word2[i]

        return merged

        #Time Complexity: O(n + m), n and m are the lengths of the strings word1 and word2 respectively
        #Space Complexity: O(n + m), n and m are the lengths of the strings word1 and word2 respectively
