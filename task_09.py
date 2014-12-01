#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Extracts files and creates sorted dictionary"""

import task_09_utility

DATA_FILES = [{'data': 'task_09_data/router_01.csv'},
              {'data': 'task_09_data/router_02.csv'},
              {'data': 'task_09_data/router_03.csv'}]

def load_data(datafiles):
    """
    Loads the files into a dictionary"""

    retval = {}
    counter = 0
    for value in datafiles:
        counter += 1
        data = task_09_utility.get_data(value['data'])
        retval[counter] = data
    return retval

def merge_data(rawdata):
    """Merges data"""
    merged = {}
    for key, value in rawdata.iteritems():
        for item in value:
            day = item['clock'][8:10]
            hour = item['clock'][11:13]
            candidate = '{}{}'.format(day, hour)
            if candidate in merged:
                merged[candidate][key] = item['value_avg']
            else:
                dummy = 0
                merged[candidate]=[item['clock']]
                while dummy < len(rawdata):
                    merged[candidate].append(0)
                    dummy += 1
                merged[candidate][key] = item['value_avg']
    return task_09_utility.sort_dict(merged)
