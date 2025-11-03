# Last updated: 11/2/2025, 8:23:24 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #answer is a list with default value of one that has same length as nums
        answer = [1] * len(nums)

        #left contains the product of all the element to the left 
        left = 1 #prefix 
        for i in range(len(nums)):
            answer[i] = left
            left *= nums[i]

        #right contains the product of all the element to the right 
        right = 1 #postfix 
        for i in range(len(nums)-1, -1, -1): #could use reversed(range(length))
            #For the index 'i', right would contain the product of all the elements to the right, and we update it accordingly 
            answer[i] *= right
            right *= nums[i]
        
        return answer 

        #Time Complexity: O(n)
        #Space Complexity: O(n)