class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        rp = len(numbers) - 1
        lp = 0
        result=[]
        while lp < rp:

            if numbers[lp] + numbers[rp] == target:
                return [lp + 1, rp + 1]
            elif numbers[lp] + numbers[rp] > target:
                rp -= 1
            else:
                lp += 1
        return result
