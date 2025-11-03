# Last updated: 11/2/2025, 8:22:28 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #store the length of s1 and s2 to use for later 
        n1 = len(s1)
        n2 = len(s2)
        #If s1 is longer than s2, s2 can't possibly contain a permutation of s1
        if n1 > n2:
            return False
        #Create frequency arrays for all lowercase letters (26 letters)
        s1Count = [0] * 26
        s2Count = [0] * 26

        #Count frequency of each character in s1 and the first window of s2
        for i in range(n1):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        #Initialize sliding window, basically maintain a fixed size window based on the size of s1 
        #len(n2) - len(s1), the number of window slides it would take to find permutations 
        for i in range(n2 - n1):
            # If all 26 character counts match, s2 contains a permutation of s1
            if s1Count == s2Count:
                return True
            
            # Shifting the window to the left by one, so we add a new character(rightside) and delete a character(leftside)
            # Character entering the window (from the right), new character on the right 
            s2Count[ord(s2[i+n1]) - ord('a')] += 1 
            
            # Character leaving the window (from the left), delete character on the left 
            s2Count[ord(s2[i]) - ord('a')] -= 1 
            #then window slides to the left 

        return s1Count == s2Count # After the loop, check if the last window matches
        
        #Time Complexity:O(n), each character is processed once in the sliding window
        #Space Complexity:O(1), both s1count and s2count are fixed-size arrays O(26)


        
