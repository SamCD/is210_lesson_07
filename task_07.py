#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creates addition function"""


def iter_dict_funky_sum(dictarg):

    """
    Sums up a dictionary in an iteresting way"""

    running_total = 0
    for key, value in dictarg.iteritems():
        running_total += value - key
    return running_total
