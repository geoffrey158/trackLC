// Last updated: 11/2/2025, 8:23:37 PM
class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        Integer candidate = null;

        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            if(num == candidate){
                count += 1;
            }
            else{ 
                count += -1;
            }
        }

        return candidate;
    }
}