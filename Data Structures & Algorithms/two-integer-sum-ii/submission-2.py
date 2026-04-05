class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        rp = len(numbers) - 1
        lp  = 0
        while lp < rp:
            sumnum = numbers[lp] + numbers[rp]
            if sumnum == target:
                return [lp + 1,rp + 1]  
            elif sumnum > target:
                rp -= 1
            else:
                lp += 1 
