# Last updated: 11/2/2025, 8:23:15 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [] #result output
        count = {} #key = number, value = frequnecy of number 

        # Create buckets: an array of empty lists
        # Index = frequency, Value = list of numbers with that frequency
        # Edge case:len(nums) + 1 buckets since max frequency = len(nums)
        freq = [[] for i in range(len(nums)+1)] 

        # Step 1: Count frequencies of each number in nums
        for n in nums: 
            count[n] = 1 + count.get(n,0)

        # Step 2: Place numbers into the corresponding frequency bucket
        # Example: if number 5 appears 3 times → freq[3].append(5)
        for n,c in count.items(): #n =element, c = frequency 
            freq[c].append(n)
        
        # Step 3: Traverse the buckets backwards (from high freq to low) and collect numbers until we have k of them
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n) 
                if len(res) == k: # stop once we have k elements in res list
                    return res

        #Time: O(n), iterates through all elements once in the worst case 
        #Space: O(n), since we use hashmap and bucket list 
            