// Last updated: 11/2/2025, 8:23:40 PM
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        

        //Two Pointers for Sorted Array
        //Time Complexity: O(N), Input array travesed at most once
        //Space Complexity: O(1). We only use additional space to store two indices and the sum,
        //so space complexity is O(1).
        
        int[] sol = new int[2];

        int left = 0;
        int right = numbers.length -1;

        while(left < right){
            int sum = numbers[left] + numbers[right];

            if(sum == target){
                sol[0] = left+1;
                sol[1] = right+1;        
                return sol;
            }
            else if(sum > target){
                right--;
            }
            else{
                left++;
            }
        }
        return null;
    }
}