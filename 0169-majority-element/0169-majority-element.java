class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        int candidate = nums[0];
        for (int num:nums) {
            if (count == 0) {
                candidate = num;
                count += 1;
            } else if (num == candidate) {
                count ++;
            } else {
                count --;
            }
            System.out.print(count);
        }
        System.out.print(candidate);
        return candidate;
    }
}