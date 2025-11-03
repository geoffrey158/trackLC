# Last updated: 11/2/2025, 8:22:23 PM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #return list, default to 0 in case there is no warmer days 
        res = [0] * len(temperatures)
        stack = []  #stores indices, stack is decreasing in temperatures
        #i - index, t - temperature
        for i, t in enumerate(temperatures):
            # While stack is not empty AND current day's temperature is warmer # than the temperature at the index on top of the stack
            while stack and t > temperatures[stack[-1]]:
                index = stack.pop()   #Index of the previous cooler day
                res[index] = i - index  #Days waited until warmer temperature

            #Push current day's index onto the stack
            stack.append(i)

        return res
    #Time Complexity O(n), Each index is pushed & popped at most once. 
    #Space Complexity O(n), For the stack and output array.