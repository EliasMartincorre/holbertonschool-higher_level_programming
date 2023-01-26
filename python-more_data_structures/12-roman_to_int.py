#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    r = roman_string
    a, b = 0, 0
    ro = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(r)):
        if ro[r[i]] <= a:
            a += ro[r[i]]
        if ro[r[i]] > a:
            a = ro[r[i]] - a
    return a
