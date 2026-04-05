class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cMax = 0
        cMin = 0
        globalMax = nums[0]
        globalMin = nums[0]
        total = 0

        for n in nums:
            cMax = max(cMax + n, n)
            cMin = min(cMin + n, n)
            total += n
            globalMax = max(globalMax, cMax)
            globalMin = min(globalMin, cMin)
        
        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax


            

            