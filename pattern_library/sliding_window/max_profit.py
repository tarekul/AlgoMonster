def maxProfit(prices: list[int]) -> int:
    # Return the largest profit from one buy and one later sell.
    best = 0
    lo = prices[0]

    for p in prices:
        if p < lo:
            lo = p
        elif p - lo > best:
            best = p - lo
    return best 

print(maxProfit([9, 2, 7, 1, 8, 3]))
print(maxProfit([10, 9, 8, 7]))
