from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Edge case: empty list
        
        num_set = set(nums)  # Store unique elements for O(1) lookups
        max_count = 0
        
        for num in num_set:
            # Only start counting if 'num' is the start of a sequence
            if num - 1 not in num_set:
                count = 1
                while num + count in num_set:
                    count += 1
                
                max_count = max(max_count, count)
        
        return max_count
