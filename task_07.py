#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creates addition function"""

DATA = {1:3, 2:20, 3:24, 4:34, 5:33, 6:1, 7:5, 8:55, 9:10, 10:11}
def iter_dict_funky_sum(dictionary):
"""
Sums up a dictionary in an iteresting way"""

    amt = 0
    for a, b in dictionary.iteritems():
        amt += (b - a)
    return amt
