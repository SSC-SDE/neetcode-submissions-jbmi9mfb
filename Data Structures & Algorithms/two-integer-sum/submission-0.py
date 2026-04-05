class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, value in enumerate(nums):
            counterpart = target - value
            if counterpart in hashmap:
                return [hashmap[counterpart], index]
            hashmap[value] = index
            
        return []