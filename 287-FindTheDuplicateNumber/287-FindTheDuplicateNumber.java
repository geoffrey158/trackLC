// Last updated: 11/2/2025, 8:23:18 PM
class Solution {
    public int findDuplicate(int[] nums) {
    
        //LinkedList - Fast and Slow Pointer 
        int slow = 0;
        int fast = 0;

        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        while (slow != fast);
        
        int slow2 = 0;
        do {
            slow = nums[slow];
            slow2 = nums[slow2];
        }
        while (slow != slow2);

        return slow2; 
        //HashSet 
        //Time complexity - O(n)
        //Space complexity - O(n)

        /*
        HashSet<Integer> dup = new HashSet<Integer>();

        for(int i:nums){
            if(dup.add(i) == false){
                return i;
            }
        }
        return 0;
        */

        //Brute Force - nested forloop
        //Time complexity - O(n^2)
        //Space complexity - O(1)
        /*
        for(int i = 0; i <nums.length-1;i++){
            for(int y = i+1; y <nums.length; y++){
                if(nums[i] == nums[y]){
                    return nums[i];
                }
            }
        }
        return 0;
        */
    }
}