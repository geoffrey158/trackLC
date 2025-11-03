// Last updated: 11/2/2025, 8:23:35 PM
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<Integer>();

        for(int i:nums){
            if(!set.add(i)){
                return true;
            }
        }
        return false;
    }
}