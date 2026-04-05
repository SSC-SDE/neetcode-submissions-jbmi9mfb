class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ma = 0
        lp = 0
        rp = len(heights)- 1

        while lp < rp:

            ca = min(heights[lp],heights[rp]) * (rp - lp)
            ma = max(ma, ca)
            
            if heights[lp] <= heights[rp]:
                lp += 1
            else:
                rp -=1

        return ma
