class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maximum=0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maximum = max(profit, maxP)
            else:
                l = r
            r+=1
        return maximum        
