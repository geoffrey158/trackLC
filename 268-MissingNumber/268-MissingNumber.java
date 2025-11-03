// Last updated: 11/2/2025, 8:23:21 PM
class Solution {
    public int missingNumber(int[] nums) {
        int lens = nums.length;
        int ans = ((lens*lens)+lens) / 2;

        for(int i = 0; i < nums.length; i++){

            ans -= nums[i];

        }
        return ans;
    }
}