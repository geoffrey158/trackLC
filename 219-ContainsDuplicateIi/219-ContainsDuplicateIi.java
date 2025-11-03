// Last updated: 11/2/2025, 8:23:33 PM
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<Integer>();
        for(int i = 0; i < nums.length; i++){
            if(i > k) { //remove element if its distance to nums[i] is not lesser than k
                set.remove(nums[i-k-1]);
            } 
            if(!set.add(nums[i])){
                return true; 
            }
            //Because all still existed elements is closer than k distance to the num[i], therefore if the add()                                                return false, it means there's a same value element already existed within the distance k, therefore return true.
        }
        return false;
    }
}