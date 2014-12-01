#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creates addition function"""

DATA = {1: 15,
        4: 18,
        159: 148,
        57: 158,
        12: 158,
        578: 1,
        152: 2,
        5: 123,
        102: 48,
        72: 299
        }

        
def iter_dict_funky_sum(dictarg):

    """
    Sums up a dictionary in an iteresting way"""

    running_total = 0
    for key, value in dictarg.iteritems():
        running_total += value - key
    return running_total
