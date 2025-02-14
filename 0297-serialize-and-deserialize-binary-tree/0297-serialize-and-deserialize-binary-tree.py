# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return ""
        queue = deque([root])
        while queue:
            curr_len = len(queue)
            for i in range(curr_len):
                curr = queue.popleft()
                if curr:
                    res.append(str(curr.val))
                    queue.append(curr.left)
                    queue.append(curr.right)
                else: #empty node
                    res.append("null")
        i = len(res) -1
        while res and res[-1] == "null":
            res.pop()
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1
        while queue and i < len(values):
            curr_node = queue.popleft()
            #left
            if i < len(values) and values[i] != "null":
                curr_node.left = TreeNode(values[i])
                queue.append(curr_node.left)
            i += 1
            #right
            if i < len(values) and values[i] != "null":
                curr_node.right = TreeNode(values[i])
                queue.append(curr_node.right)
            i += 1
        return root
                


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))