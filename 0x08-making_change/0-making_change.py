#!/usr/bin/python3
"""
been give a pile of coins of different values,
find the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Calculates fewest number of coins needed
    to meet a given amount total
    Args:
        coins: A list of coin values (integers greater than 0).
        total: The target amount to make change for.
    """
    coins.sort(reverse=True)  # Sort coins in descending order

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
