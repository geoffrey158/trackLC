# Last updated: 11/2/2025, 8:22:24 PM
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] 
        totalSum = 0 #tracker for totalSum 
        for i in operations:
            if i == "+":#add the sum of previous two scores and add to stack
                totalSum += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif i == "D": #double the previous score and add to stack 
                totalSum += stack[-1] * 2
                stack.append(stack[-1]*2)
            elif i == "C": #invalidate the previous score, remove it from the record
                totalSum -= stack.pop()
            else:#if it's a regular integer add to stack and change the totalSum 
                totalSum += int(i)
                stack.append(int(i))

        return totalSum

        #Time Complexity: O(n)
        #Space Complexity: O(n)