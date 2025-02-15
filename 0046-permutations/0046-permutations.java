class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> currRes = new ArrayList<>();
        
        dfs(nums, res, currRes);
        return res;
    }
    
    public void dfs(int[] nums, List<List<Integer>> res, List<Integer> currRes) {
        if (currRes.size() == nums.length) {
            res.add(new ArrayList<>(currRes));
            return;
        }
        
        for (int n : nums) {
            if (!currRes.contains(n)) {
                currRes.add(n);
                dfs(nums, res, currRes);
                currRes.remove(currRes.size() - 1);
            }
        }
    }
}