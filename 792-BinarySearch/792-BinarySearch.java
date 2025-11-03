// Last updated: 11/2/2025, 8:22:25 PM
class Solution {
    public int search(int[] nums, int target) {
        
        int left = 0;
        int right = nums.length-1;

        while(left<=right){

            int mid = (left+right)/2;
            if(nums[mid] == target){
                return mid; 
            }
            else if(nums[mid]>target){
                right = mid-1;
            }
            else if(nums[mid]<target){
                left = mid+1;
            }
        
        }
        return -1;

    }
}

//Time complexity: O(log⁡n). nums is divided into half each time. In the worst-case scenario, we need to cut nums until the range has no element, and it takes logarithmic time to reach this break condition.
//Space complexity: O(1). During the loop, we only need to record three indexes, left, right, and mid, they take constant space.