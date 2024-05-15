#!/usr/bin/python3
"""log parsing module"""
import sys
import re
import signal


def signal_handler(sig, frame):
    """sigint handler"""
    sys.exit()


signal.signal(signal.SIGINT, signal_handler)
reg_exp = r"[\d\.]+[]\d\-\.:\s[]+\"GET /projects/260 HTTP/1.1\"[\d\s]+"
allowed_code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
file_size = 0
total_lines = 0
try:
    for line in sys.stdin:
        gateman = re.match(reg_exp, line)
        '''if line doesn't match regex expression, skip it'''
        if gateman.group(0) == line:
            total_lines += 1
            file_size += int(line.split()[-1])
            status_code = line.split()[-2]
            if int(status_code) in allowed_code:
                allowed_code[int(status_code)] += 1

        if (total_lines % 10 == 0):
            print("File size:", file_size)
            for key, value in allowed_code.items():
                if value > 0:
                    print("{}: {}".format(key, value))
except KeyboardInterrupt:
    # print("KeyboardInterrupt")
    signal_handler(signal.SIGINT, None)
