#!/usr/bin/python3
'''minimum number of coins module
'''


def makeChange(coins, total):
    '''finds fewest number of coins needed to meet total
    '''
    if total <= 0:
        return 0
    total2 = total
    coins.sort()
    count = []
    while coins:
        current_coin = coins.pop()
        while total2 >= current_coin:
            total2 -= current_coin
            count.append(current_coin)
    count_sum = sum(count)
    if count_sum != total:
        return -1
    return len(count)
