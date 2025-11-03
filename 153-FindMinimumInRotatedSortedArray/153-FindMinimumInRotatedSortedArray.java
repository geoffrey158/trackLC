// Last updated: 11/2/2025, 8:23:43 PM
class Solution {
    public int findMin(int[] nums) {

        //Binary Search
        //Time Complexity : Same as Binary Search O(log⁡N)
        //Space Complexity : O(1)
        int left = 0;
        int right = nums.length - 1;

        while(left<=right){
            int mid = (left+right)/2;
            if(nums[mid] > nums[nums.length-1]){
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }
        }

        return nums[left];
    }
}