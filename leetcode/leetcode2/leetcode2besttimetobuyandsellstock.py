import math

def max_stock_profit(prices: list[int]) -> int:
    max_profit = 0
    cumulative_min_price = math.inf
    for index, price in enumerate(prices):
        if price < cumulative_min_price:
            cumulative_min_price = price
        if price - cumulative_min_price > max_profit:
            max_profit = price - cumulative_min_price
    return max_profit

def max_stock_profit_yt(prices: list[int]):
    left_index, right_index = 0, 1
    max_profit = 0
    while right_index != len(prices):
        if prices[left_index] < prices[right_index]:
            profit = prices[right_index] - prices[left_index]
            max_profit = max(max_profit, profit)
        else:
            left_index = right_index
        right_index += 1
    return max_profit


if __name__ == '__main__':
    print(max_stock_profit([7, 1, 5, 3, 6, 4]))
    print(max_stock_profit([9, 7, 5, 4, 1]))
    print(max_stock_profit([1, 2, 0, 3, -1, 4]))
    print(max_stock_profit_yt([7, 1, 5, 3, 6, 4]))
    print(max_stock_profit_yt([9, 7, 5, 4, 1]))
    print(max_stock_profit_yt([1, 2, 0, 3, -1, 4]))

