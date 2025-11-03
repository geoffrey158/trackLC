// Last updated: 11/2/2025, 8:22:20 PM
class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        // Initalize the left and right boundaries 
        int left = 1;
        int right = 1;
        for (int pile : piles) {
            right = Math.max(right, pile);
        }

        while (left < right) {
            // Get the mid index between left and right boundary indexes.
            // hourSpent stands for the total hour Koko spends.
            int mid = (left + right) / 2;
            int hourSpent = 0;

            // Iterate over the piles and calculate hourSpent.
            // We increase the hourSpent by ceil(pile / mid)
            for (int pile : piles) {
                hourSpent += Math.ceil((double) pile / mid);
            }

            // Check if mid is a workable speed, and cut the search space by half.
            if (hourSpent <= h) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        // Once the left and right boundaries coincide, we find the target value,
        // that is, the minimum workable eating speed.
        return right;
    }
}