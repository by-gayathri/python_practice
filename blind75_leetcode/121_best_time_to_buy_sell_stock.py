class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit


obj = Solution()
price_list = [7, 1, 5, 3, 6, 4]
maximum_profit = obj.maxProfit(price_list)
print(f"Maximum profit you can achieve from the transaction is {maximum_profit}")

# Time Complexity: O(n) – Single pass through the array.
# Space Complexity: O(1) – Only a couple of variables used.
