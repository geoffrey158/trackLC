# Last updated: 11/28/2025, 11:25:18 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        #Step 1: defaultdict to store lists of anagrams based on their sorted representation
4        # defaultdict(list) automatically creates an empty list if the key doesn’t exist yet
5        res = defaultdict(list)
6
7        # Step 2: Iterate through each word in the input list
8        for word in strs:
9
10            # Create a list of 26 zeros to count occurrences of each lowercase letter
11            count = [0] * 26 
12
13            # Count how many times each letter appears in the word
14            for c in word:
15                # ord(ch) - ord('a') gives an index between 0 and 25
16                count[ord(c) - ord('a')] += 1
17
18            # Convert the list to a tuple (since lists can't be dictionary keys)
19            # Words with identical letter counts will produce the same tuple
20            # Then add the word to the correct group in the dictionary
21            res[tuple(count)].append(word)
22
23        # Convert the dictionary values to a list of lists and return
24        return list(res.values())
25
26        #Time Complexity:O(m*n), Where m is the number of strings and n is the length of the longest string.
27        #Space Complexity:O(m) extra space. O(m∗n) space for the output list