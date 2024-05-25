#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

'''# custom
data = [36]
print(validUTF8(data))
data = [194, 163]
print(validUTF8(data))
data = [208, 152]
print(validUTF8(data))
data = [224, 164, 185]
print(validUTF8(data))
data = [226, 130, 172]
print(validUTF8(data))
data = [237, 149, 156]
print(validUTF8(data))
data = [240, 144, 141, 136]
print(validUTF8(data))
data = [244, 137, 154, 179]
print(validUTF8(data))
# false data
data = [244, 36, 137, 154, 179]
print(validUTF8(data))
'''
print('***********Where I failed***********')
data = [467, 133, 108]
print(validUTF8(data))
data = [235, 140]
print(validUTF8(data))
