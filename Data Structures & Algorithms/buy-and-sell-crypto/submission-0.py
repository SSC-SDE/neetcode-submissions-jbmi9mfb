class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        mp = 0

        while right < len(prices):

            cp = prices[right] - prices[left]

            if prices[left] > prices[right]:
                left = left + 1
            else:
                mp = max(mp, cp)
                right = right + 1
        
        return mp