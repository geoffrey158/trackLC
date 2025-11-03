# Last updated: 11/2/2025, 8:22:26 PM
class Solution:
    def validPalindrome(self, s: str) -> bool:
        #function used to find if a string is a palindrome based on two pointers
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0 
        right = len(s) - 1 

        while left < right:
            #if left is not equal to right 
            if s[left] != s[right]:
                #check if the left is deleted by one 
                #check if the right is deleted by one 
                #if either one is true that means deleting a character makes a palindrome
                return (is_palindrome(left + 1, right) or 
                        is_palindrome(left, right - 1))
            left += 1
            right -= 1

        return True

        #Time complexity: O(n)
        #Space complexity: O(1)
            
                
