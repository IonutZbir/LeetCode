from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()  # Ordinare aiuta: a | b implica che a <= b

        # Costruzione del grafo: arco tra ogni coppia divisibile
        graph = {n: set() for n in nums}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0:
                    graph[nums[i]].add(nums[j])
                    graph[nums[j]].add(nums[i])

        best_clique = []

        def is_connected_to_all(node, clique):
            return all(node in graph[other] for other in clique)

        def expand(clique, candidates):
            nonlocal best_clique

            if len(clique) > len(best_clique):
                best_clique = clique[:]

            for i, node in enumerate(candidates):
                if is_connected_to_all(node, clique):
                    expand(clique + [node], candidates[i+1:])

        nodes = sorted(nums, key=lambda x: -len(graph[x]))  # ordine euristico
        expand([], nodes)

        return best_clique
