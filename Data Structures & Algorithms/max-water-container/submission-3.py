class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        rp = len(heights) - 1
        lp = 0
        while lp < rp:

            currArea = min(heights[lp], heights[rp]) * (rp -lp)
            maxArea = max(maxArea, currArea)
            
            if heights[lp] <= heights[rp]:
                lp += 1
            else:
                rp -= 1


        return maxArea 
        