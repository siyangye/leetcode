# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph=defaultdict(list)
        queue=deque([root])
        while queue:
            curr_node = queue.popleft()
            if curr_node.left:
                graph[curr_node].append(curr_node.left)
                graph[curr_node.left].append(curr_node)
                queue.append(curr_node.left)

            if curr_node.right:
                graph[curr_node].append(curr_node.right)
                graph[curr_node.right].append(curr_node)
                queue.append(curr_node.right)
        res=[]
        visited = set([target])
        # visited.add(target)#use add() for set
        step_queue = deque([(target,0)])
        while step_queue:
            node,step = step_queue.popleft()#debug
            if step==k:
                res.append(node.val)
            else:
                for nodes in graph[node]:#its connected node in a list
                    if nodes not in visited:
                        visited.add(nodes)
                        step_queue.append((nodes,step+1))
        return res

            

            
                
            
        