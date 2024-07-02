#!/usr/bin/python3
'''game of prime numbers
'''


def find_prime(number):
    '''finds prime_numbers in number
    '''
    primes = []
    allowed = [2, 3, 5, 7]
    if number <= 1:
        return []
    for i in range(2, number + 1):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            if i in allowed:
                primes.append(i)
        else:
            primes.append(i)
    return primes


def isWinner(x, nums):
    '''finds the winne of prime games
    '''
    win_bucket = []
    for index in range(x):
        number = 0
        '''if index >= len(nums) and not win_bucket:
            return None'''
        if index >= len(nums):
            break
        current_number = nums[index]
        numbers = [x for x in range(1, current_number + 1)]
        primes = find_prime(current_number)
        # print('primes -> {}'.format(primes));
        while primes:
            value = primes.pop(0)
            for val in numbers:
                if val % value == 0:
                    numbers.remove(val)
            number += 1
        if number == 0 or number % 2 == 0:
            win_bucket.append('ben')
            # print('{}round: ben'.format(index + 1))
        else:
            win_bucket.append('maria')
            # print('{}round: maria'.format(index + 1))
    ben_count = win_bucket.count('ben')
    maria_count = win_bucket.count('maria')
    if ben_count > maria_count:
        return 'Ben'
    if maria_count > ben_count:
        return 'Maria'
    else:
        return None
