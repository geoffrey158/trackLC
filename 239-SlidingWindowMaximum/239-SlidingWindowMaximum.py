# Last updated: 11/2/2025, 8:23:23 PM
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Monotonic Deque problem, keep deque in decreasing order of values
        res = [] #return value, list to store the maximum of each sliding window

        #sliding window technique
        left = 0 
        right = 0 
        dq = deque() # will store indices of elements, not the elements themselves

        # Traverse through the array using the right pointer
        while right < len(nums):
            #Remove elements from the back that are smaller than current element
            #This ensures the deque stores indices in decreasing order of values
            while dq and nums[right] >= nums[dq[-1]]:
                dq.pop()
            
            dq.append(right) #Add current index to the deque

            # Remove indices from the front if they are outside the window's left boundary
            if left > dq[0]:
                dq.popleft()

            #right window gets added
            if (right+1) >= k:
                res.append(nums[dq[0]]) #dq[0] is always the max in the current window because we use deque to maintain that
                left += 1 #Move the left side of the window forward
            right += 1 #Move the right side of the window forward

        return res 

        #Time complexity:O(n), Each element is added to the deque exactly once and removed at most once. Appending to or removing from deque is O(1) (amortized).
        #Space complexity:O(k), The deque stores indices of elements within a window of size k, and at most k elements can be in the deque.