# Last updated: 11/2/2025, 8:23:19 PM
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        #Sorted by the keys and not the values of the keys 
        intervals.sort() #O(nlogn) time

        for i in range (len(intervals)-1):
            #Check if the ending time of meeting 1 overlaps the starting time of next meeting
            #This works cause list is already sorted 
            if intervals[i][1] > intervals[i+1][0]: 
                return False 
        
        return True 

        """
        Sorting
        Time Complexity: O(nlogn), due to using sort(), if the array is already sorted it only takes O(n) to go 
        through the array
        Space Complexity: O(1), no additonal space is used

        """

        """
        Brute Force 
        Compare every two meetings in the array and see if they conflict with each otehr 

        Time Complexity:O(n^2), nested for loop to check every meeting with every other meeting 
        Space Complexity:O(1), no additional space is used 

        """
        """
        def overlap(interval1: List[int], interval2: List[int]) -> bool:
            return (interval1[0] >= interval2[0] and interval1[0] < interval2[1]
                or interval2[0] >= interval1[0] and interval2[0] < interval1[1])

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if overlap(intervals[i], intervals[j]):
                    return False
        return True
        """
