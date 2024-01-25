#!/usr/bin/python3
"""Parses log parsing"""
from sys import stdin


def print_stats(status_code, size):
    """function that prints stat"""
    print("File size: {size}".format(size=size))
    for code in sorted(status_code):
        if status_code.get(code) != 0:
            print("{c}: {v}".format(c=code, v=status_code.get(code)))


i = 0
size = 0
status_code = {"200": 0, "301": 0, "400": 0, "401": 0,
               "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for line in stdin:
        line = line.rstrip()
        line = line.split(" ")
        if len(line) > 2:
            line.reverse()
            code = line[1]
            size += int(line[0])

            if code in status_code.keys():
                status_code.update({code: status_code.get(code) + 1})

            i += 1

            if i % 10 == 0:
                print_stats(status_code, size)
finally:
    print_stats(status_code, size)

