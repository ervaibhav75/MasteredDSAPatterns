from typing import List

class Solution:
    '''
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in  the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    video: https://www.youtube.com/watch?v=excAOvwF_Wk
    '''
    
    def maxProfit(self, prices: List[int]) -> int:
        #minimum is frst now we keep updating minumum onwards
        minimum = prices[0]
        max_profit = -1

        for i in prices:
            #then try to get profit by substracting the min from current
            profit = i - minimum
            max_profit = max(profit, max_profit)
            minimum = min(minimum , i)
            
        return max_profit
