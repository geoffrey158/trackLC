// Last updated: 11/2/2025, 8:22:29 PM
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> result = new ArrayList<Integer>();
        Set<Integer> set = new HashSet<Integer>();

        for(int n: nums){
            if(!set.add(n)){
                result.add(n);
            }
        }


        return result;
    }
}