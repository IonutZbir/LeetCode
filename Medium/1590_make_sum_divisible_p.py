from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p
        
        # If total sum is already divisible by p, no need to remove any subarray
        if remainder == 0:
            return 0
        
        # Dictionary to store the prefix sum modulo p and their indices
        prefix_mod = {0: -1}
        prefix_sum = 0
        min_len = len(nums)
        
        for i, num in enumerate(nums):
            prefix_sum += num
            mod = prefix_sum % p
            target = (mod - remainder) % p
            
            if target in prefix_mod:
                min_len = min(min_len, i - prefix_mod[target])
            
            # Store current prefix sum modulo p
            prefix_mod[mod] = i
        
        print(prefix_mod)
        
        # If no valid subarray found, return -1
        return min_len if min_len < len(nums) else -1

# Example usage:
s = Solution()
print(s.minSubarray([3, 1, 4, 2], 6))  # Output: 1
