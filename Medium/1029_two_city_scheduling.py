from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return sum(map(lambda cost: min(cost[0], cost[1]), costs))