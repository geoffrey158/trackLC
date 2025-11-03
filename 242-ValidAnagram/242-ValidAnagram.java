// Last updated: 11/2/2025, 8:23:24 PM
class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        //Using a Counter
        /*
        Creates a size 26 int arrays as buckets for each letter in alphabet. 
        It increments the bucket value with String s and decrement with string t. 
        So if they are anagrams, all buckets should remain with initial value which is zero. 
        Checks if all the buckets are 0 at the end, if it is true, if not it's false
        */

        int[] store = new int[26];

        for (int i = 0; i < s.length(); i++) {
            //'a' just gives you distance between 'a' and the character which is nothing but index value of freq array
            //'a' = 0, 'b' = 1, 'c' = 2.... 
            store[s.charAt(i) - 'a']++; 
            store[t.charAt(i) - 'a']--; 
        }

        for (int n : store){
            if (n != 0){
                return false;
            }
        }

        return true;
    }
}

//Time Complexity: O(n), accessing the counter table is a constant time operation 
//Space complexity: O(1). space complexity is O(1) because the table's size stays constant no matter how large n is.