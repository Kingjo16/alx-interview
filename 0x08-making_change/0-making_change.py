#!/usr/bin/python3
"""Coin change solution module."""


def makeChange(denominations, target_amount):
    """Determine the num of coins in a pile."""
    if target_amount <= 0:
        return 0

    remaining_amount = target_amount
    total_coins = 0
    denom_index = 0
    sorted_denominations = sorted(denominations, reverse=True)
    num_denominations = len(denominations)

    while remaining_amount > 0:
        if denom_index >= num_denominations:
            return -1
        if remaining_amount - sorted_denominations[denom_index] >= 0:
            remaining_amount -= sorted_denominations[denom_index]
            total_coins += 1
        else:
            denom_index += 1

    return total_coins
