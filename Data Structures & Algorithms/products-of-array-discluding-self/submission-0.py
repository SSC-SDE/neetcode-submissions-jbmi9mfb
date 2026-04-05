from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n  # Step 1: Initialize output array with 1

        # Step 2: Compute Prefix Products
        prefix = 1
        for i in range(n):
            output[i] = prefix  # Store prefix product (product of all elements to the left)
            prefix *= nums[i]   # Update prefix by multiplying current element

        # Step 3: Compute Suffix Products and Multiply
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix  # Multiply with suffix product (product of all elements to the right)
            suffix *= nums[i]    # Update suffix by multiplying current element

        return output
