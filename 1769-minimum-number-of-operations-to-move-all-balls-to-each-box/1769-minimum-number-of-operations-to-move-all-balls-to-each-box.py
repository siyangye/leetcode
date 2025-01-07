class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n
        
        # 计算左边小球的影响
        count = 0  # 左边小球的数量
        operations = 0  # 累计操作数
        for i in range(n):
            result[i] += operations
            count += int(boxes[i])
            operations += count  # 更新操作数
        
        # 计算右边小球的影响
        count = 0  # 重置为右边小球的数量
        operations = 0  # 重置累计操作数
        for i in range(n-1, -1, -1):
            result[i] += operations
            count += int(boxes[i])
            operations += count  # 更新操作数
        
        return result