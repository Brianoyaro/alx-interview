#!/usr/bin/python3
"""log parsing module"""
import sys
import re


reg_exp = r"[\d\.]+[]\d\-\.:\s[]+\"GET /projects/260 HTTP/1.1\"[\d\s]+"
allowed_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
lines = sys.stdin.read()
lines = lines.split('\n')
file_size = 0
i = 10
terminate_point = 0
try:
    while lines[-1] != lines[terminate_point]:
        group = []
        mark = 0
        while mark < i:
            line = lines[mark]
            gateman = re.match(reg_exp, line)
            '''if line doesn't match regex expression, skip it'''
            if gateman.group(0) != line:
                continue
            file_size += int(line.split()[-1])
            status_code = line.split()[-2]
            if int(status_code) in allowed_status_codes:
                group.append(status_code)
            mark += 1
        # write logic for grouping and mapping each status_code to its count
        unique_set = list(set(group))
        unique_set.sort()
        mapper = {}
        for val in unique_set:
            sum_ = group.count(val)
            mapper[val] = sum_
        # first print File size: file_size -> line 21
        print("File size: {}".format(file_size))
        # then print all mapped values
        for key, value in mapper.items():
            print("{}: {}".format(key, value))
        i += 10
        terminate_point += 10
except KeyboardInterrupt as e:
    print(e)
