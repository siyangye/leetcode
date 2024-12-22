# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #base case 
        if not root: #遍历到最后一层节点，但还是没有找到 
            return None
        if root==p or root==q: #check节点本身是不是target的p/ q node 
            return root
        #recursive case: 这个node还有子节点，而且我们还没有找到target
        left_res = self.lowestCommonAncestor(root.left,p,q)
        right_res = self.lowestCommonAncestor(root.right,p,q)

        if left_res and right_res: #左右子树分别有一个p&q -> 左右子树的root肯定是共同祖先了
            return root 
        elif left_res: 
            return left_res #其实就是return了我们寻找到了的节点,p或者q
        else:
            return right_res #同上 
        