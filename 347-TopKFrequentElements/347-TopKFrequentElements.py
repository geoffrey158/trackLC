# Last updated: 11/28/2025, 11:34:24 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        res = [] #result output
4        count = {} #key = number, value = frequnecy of number 
5
6        # Create buckets: an array of empty lists
7        # Index = frequency, Value = list of numbers with that frequency
8        # Edge case:len(nums) + 1 buckets since max frequency = len(nums)
9        freq = [[] for i in range(len(nums)+1)] 
10
11        # Step 1: Count frequencies of each number in nums
12        for n in nums: 
13            count[n] = 1 + count.get(n,0)
14
15        # Step 2: Place numbers into the corresponding frequency bucket
16        # Example: if number 5 appears 3 times → freq[3].append(5)
17        for n,c in count.items(): #n =element, c = frequency 
18            freq[c].append(n)
19        
20        # Step 3: Traverse the buckets backwards (from high freq to low) and collect numbers until we have k of them
21        for i in range(len(freq)-1,-1,-1):
22            for n in freq[i]:
23                res.append(n) 
24                if len(res) == k: # stop once we have k elements in res list
25                    return res
26
27        #Time: O(n), iterates through all elements once in the worst case 
28        #Space: O(n), since we use hashmap and bucket list 
29            