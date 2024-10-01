from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cur = [0]
        for i in range(nums):
            self.cur.append(self.nums[i] + self.cur[-1])


    def sumRange(self, left: int, right: int) -> int:
        return self.cur[right + 1] - self.cur[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)