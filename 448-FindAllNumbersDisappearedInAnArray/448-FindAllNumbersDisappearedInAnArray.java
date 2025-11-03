// Last updated: 11/2/2025, 8:22:33 PM
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        ArrayList<Integer> result = new ArrayList<Integer>();

        HashSet<Integer> set = new HashSet<Integer>();
        for(int i = 1 ; i<nums.length+1;i++){
            set.add(i);
        }


        for(int x = 0; x<nums.length;x++){
            set.remove(nums[x]);
        }

        for(int temp: set){
            result.add(temp);
        }

        return result;
    }
}