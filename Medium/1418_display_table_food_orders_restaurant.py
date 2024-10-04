# Problem: https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

from typing import List

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        orders.sort(key= lambda x: int(x[1]))
        
        food_list = set(x[2] for x in orders)
        food_list = list(food_list)
        food_list.sort()
        food_list.insert(0, "Table")
        
        freq_map = {}
        table_map = {}
        
        for _, table, food in orders:
            freq = freq_map.get((table, food), 0)
            freq_map[(table, food)] =  freq + 1
        
        for table, food in freq_map:
            table_map[table] = 1

        table_list = list(table_map.keys())
        table_list.sort()
        
        result = []
        result.append(food_list)
        for table in table_list:
            row = [table]
            for food in food_list[1:]:
                freq = freq_map.get((table, food), 0)
                row.append(str(freq))
            result.append(row)

        result[1:] = sorted(result[1:], key=lambda x: int(x[0]))
        return result


s = Solution()

orders = [
    ["David", "3", "Ceviche"],
    ["Corina", "10", "Beef Burrito"],
    ["David", "3", "Fried Chicken"],
    ["Carla", "5", "Water"],
    ["Carla", "5", "Ceviche"],
    ["Rous", "3", "Ceviche"]
]

k = s.displayTable(orders)
print(k)
