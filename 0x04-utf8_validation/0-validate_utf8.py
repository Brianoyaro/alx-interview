#!/usr/bin/python3
'''utf-8validation
'''
import re
from typing import List


def binary_function(n: int) -> str:
    '''returns a binary representation of a number
    '''
    bin_n = bin(n)[2:]

    offset = len(bin_n) - 8
    if offset > 0:
        bin_n = bin_n[offset:]

    padding = 8 - len(bin_n)
    for _ in range(padding):
        bin_n = '0' + bin_n
    return bin_n


def check_type(s: str) -> int:
    '''finds type of code point associated with a byte
    '''
    type_1_regex = r"^0[\d]{7}"
    type_2_regex = r"^110[\d]{5}"
    type_3_regex = r"^1110[\d]{4}"
    type_4_regex = r"^11110[\d]{3}"
    val = re.match(type_1_regex, s)
    if val is not None:
        return 1
    val = re.match(type_2_regex, s)
    if val is not None:
        return 2
    val = re.match(type_3_regex, s)
    if val is not None:
        return 3
    val = re.match(type_4_regex, s)
    if val is not None:
        return 4
    return -1


def is_next_valid(data: List) -> bool:
    '''validates next data set byte
    '''
    val = data.pop(0)
    bin_item = binary_function(val)
    check = re.match(r'^10[\d]{6}', bin_item)
    '''if check is None:
        return False
    return True
    '''
    return check


def validUTF8(data: List[int]) -> bool:
    '''determines if a given data set represents a valid UTF-8 encoding
    '''
    while data:
        item = data.pop(0)
        '''byte can range from 0 - 255
        '''
        '''if item > 255:
            return False'''
        bin_item = binary_function(item)
        type_item = check_type(bin_item)
        if type_item == 1:
            continue
        if type_item == 2:
            '''next item should comply
            '''
            if data:
                check = is_next_valid(data)
                if check is None:
                    return False
            else:
                return False
        if type_item == 3:
            '''next 2 items should comply
            '''
            for _ in range(2):
                if data:
                    check = is_next_valid(data)
                    if check is None:
                        return False
                else:
                    return False

        if type_item == 4:
            '''next 3 items should comply
            '''
            for _ in range(3):
                if data:
                    check = is_next_valid(data)
                    if check is None:
                        return False
                else:
                    return False
        if type_item == -1:
            return False
    return True
