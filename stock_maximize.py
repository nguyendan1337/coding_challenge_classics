def stockmax(prices):
    # Write your code here
    current_max = 0
    profit = 0

    for price in reversed(prices):
        if price > current_max:
            current_max = price
        else:
            profit += current_max - price

    return profit

# def stockmax(prices):
#     # Write your code here
#     print(f"prices: {prices}")
#     portfolio = 0
#     stocks = 0
#     profit = 0
#     length = len(prices)
#
#     if prices[0] < prices[1]:
#         portfolio += prices[0]
#         stocks += 1
#     for i in range(1,length-1):
#         action = ""
#         #sell
#         if prices[i-1] < prices[i] and prices[i] >= prices[i+1]:
#             profit += prices[i]*stocks - portfolio
#             stocks = 0
#             portfolio = 0
#             action = "sell"
#         #buy
#         elif prices[i-1] > prices[i] and prices[i] <= prices[i+1]:
#             stocks += 1
#             portfolio += prices[i]
#             action = "buy"
#         elif prices[i-1] < prices[i] and prices[i] < prices[i+1]:
#             stocks += 1
#             portfolio += prices[i]
#             action = "buy"
#         print(f"prices[{i}]: {prices[i]} {action}")
#     if prices[length-1] > prices[length-2]:
#         profit += stocks*prices[length-1] - portfolio
#     print(profit)
#     return profit


prices = [5, 4, 3, 4, 5]
print(stockmax(prices))  # Output: 4