# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Fishka: Keep track of the minimum price seen so far and calculate the potential profit at each step.
# Fishka: Sliding window approach.

from typing import List

class MyBruteForceSolution:
    def maxProfit(self, prices: List[int]) -> int:

        global_max_profit = 0
        for buy_idx, buy_price in enumerate(prices):
            for sell_idx in range(buy_idx + 1, len(prices)):
                sell_price = prices[sell_idx]
                curr_max_profit = (sell_price - buy_price)
                # These conditions are not necessary since negative curr_mux_profit will never beat global_max_profit
                # if sell_price < buy_price:
                #     curr_max_profit = (sell_price - buy_price)
                # if curr_max_profit <= 0:
                #     continue
                if curr_max_profit > global_max_profit:
                    global_max_profit = curr_max_profit

        return global_max_profit
    

class MyUnconventionalSolution:
    def maxProfit(self, prices: List[int]) -> int:

        max_roi = 0
        best_buy = prices[0]
        for buy_idx, buy_price in enumerate(prices):
            if buy_price < best_buy:
                best_buy = buy_price
            sell_idx = buy_idx + 1

            if sell_idx < len(prices):
                sell_price = prices[sell_idx]
            else:
                return max_roi

            if sell_price < best_buy:
                continue
            else:
                curr_roi = sell_price - best_buy
                if curr_roi > max_roi:
                    max_roi = curr_roi

        return max_roi


class ConventionalSolution:
    def maxProfit(self, prices: List[int]) -> int:

        max_roi = 0
        best_buy = prices[0]

        for curr_price in prices:
            best_buy = min(best_buy, curr_price)
            max_roi = max(max_roi, curr_price - best_buy)
        
        return max_roi 

