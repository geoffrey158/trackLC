# Last updated: 12/7/2025, 6:51:13 AM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        #return list, Default is 0 because if there's no future warmer day, answer stays 0.
4        res = [0] * len(temperatures) 
5        stack = []  #stores indices, monotonic *decreasing* used to store the INDICES of tempeatures
6
7        #loop throught each index and temperature 
8        for idx, temp in enumerate(temperatures):
9
10            # While stack is not empty AND current day's temperature is warmer # than the temperature at the index on top of the stack
11            # That means we found a warmer future day for stack[-1]
12            while stack and temp > temperatures[stack[-1]]:
13                index = stack.pop()   #Index of the previous cooler day
14                res[index] = idx - index  #Days waited until warmer temperature
15
16            # Push current day's index onto the stack
17            # That means we found a warmer future day for stack[-1].
18            stack.append(idx)
19
20        return res
21    #Time Complexity O(n), Each index is pushed & popped at most once. 
22    #Space Complexity O(n), For the stack and output array.