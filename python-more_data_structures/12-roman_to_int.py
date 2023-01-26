#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    r = roman_string
    a = 0
    ro = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(r)):
        if i > 0 and ro[r[i]] > ro[r[i - 1]]:
            a += ro[r[i]] - 2 * ro[r[i - 1]]
        else:
            a += ro[r[i]]
    return a
