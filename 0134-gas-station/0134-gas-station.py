class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        min_gas = float('inf')
        curr_gas = start = 0
        for i in range(len(gas)):
            curr_gas = curr_gas + gas[i] - cost[i]
            if min_gas > curr_gas:
                min_gas = curr_gas
                start = i
        #start 
        if start == len(gas)-1:
            return 0
        else:
            return start + 1