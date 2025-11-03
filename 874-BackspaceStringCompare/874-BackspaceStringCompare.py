# Last updated: 11/2/2025, 8:22:18 PM
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        countS = len(s)-1 #Traverse from the end of s and t
        countT = len(t)-1 
        backS = 0 # The number of backspaces required till we arrive at a valid character for s and t
        backT = 0 

        while countS >= 0 or countT >= 0: 

            while countS >= 0: # Ensure that we are comparing a valid character in s
                if s[countS] == "#":
                    backS += 1 
                    countS -= 1
                elif backS > 0:
                    backS -= 1 #Backspace the number of times calculated in the previous step
                    countS -= 1 
                else:
                    break
            
            while countT >= 0:# Ensure that we are comparing a valid character in t
                if t[countT] == "#":
                    backT += 1 
                    countT -= 1
                elif backT > 0:
                    backT -= 1# Backspace the number of times calculated in the previous step
                    countT -= 1  
                else:
                    break

            print("Comparing", s[countS], t[countT])		# Print out the characters for better understanding.

            if countS >= 0 and countT >= 0 and s[countS] != t[countT]: #Compare both valid characters 
                return False

            if (countS>=0) != (countT>=0):#Ensures that both the character indices are valid.
                return False

            countS -= 1 
            countT -= 1 

        return True 