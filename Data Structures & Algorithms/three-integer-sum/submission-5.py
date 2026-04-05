class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result =[]      
        nums.sort()
        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            lp = i + 1
            rp = len(nums)- 1

            while lp < rp:

                checkSum = nums[i] + nums[lp] + nums[rp]
                if checkSum == 0:                   
                    result.append([nums[i], nums[lp], nums[rp]])                  
                    while lp < rp and nums[lp] == nums[lp + 1]:
                        lp += 1
                    while lp < rp and nums[rp] == nums[rp - 1]:
                        rp -= 1

                    lp += 1
                    rp -= 1
                elif checkSum < 0:
                    lp += 1
                else:
                    rp -= 1
        
        return result

