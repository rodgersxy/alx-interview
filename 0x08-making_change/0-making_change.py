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
    if total <= 0:
        return 0
    change = 0
    coins.sort(reverse=True)
    for coin in coins:
        temp_change = int(total / coin)
        total -= (temp_change * coin)
        change += temp_change
        if total == 0:
            return change
    if total != 0:
        return -1
