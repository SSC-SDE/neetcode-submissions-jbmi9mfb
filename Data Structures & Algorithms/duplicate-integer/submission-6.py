class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = Counter(nums)
        for i in res:
            if res[i] > 1:
                return True
        
        return False