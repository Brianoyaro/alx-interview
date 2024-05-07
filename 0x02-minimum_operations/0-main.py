#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
print("Min # of operations to reach {} char: {}".format(17, minOperations(17)))
n=120
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n=9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n=1001
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n=3
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n=91
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n=13
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
