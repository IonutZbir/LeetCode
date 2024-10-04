from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        
        if n == 0:
            return 0
        
        if n == 2:
            return skill[0] * skill[1]
        
        skill.sort()
        
        number_of_teams = n // 2
        teams = []
        
        j = n - 1
        for i in range(n):
            teams.append((skill[i], skill[j]))
            j -= 1
        
        teams = teams[:number_of_teams]
        
        total_skill = 0
        prev = teams[0][0] + teams[0][1]
        for i, j in teams:
            if prev != i + j:
                return -1
            total_skill += i * j 
        
        return total_skill
        

s = Solution()
k = s.dividePlayers([3,2,5,1,3,4])
print(k)        