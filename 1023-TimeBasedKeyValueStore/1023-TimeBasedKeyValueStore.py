# Last updated: 11/2/2025, 8:22:08 PM
class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value,timestamp])


    def get(self, key: str, timestamp: int) -> str:
        #return value that timestamp_prev <= timestamp 
        res = "" 
        values = self.hashmap.get(key,[])
        left = 0 
        right = len(values)-1 

        while left <= right:
            mid = left + (right-left)//2
            if values[mid][1] <= timestamp: #if timestamp_prev <= timestamp
                left = mid + 1 
                res = values[mid][0]
            else:
                right = mid - 1 
        
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)