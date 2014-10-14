#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Extracts files and creates sorted dictionary"""

import task_09_utility
DATA_FILES = [{'data': 'task_09_data/router_01.csv'},
              {'data': 'task_09_data/router_02.csv'},
              {'data': 'task_09_data/router_03.csv'}]

def load_data(listobj):


    """
    Loads the files into a dictionary"""

    dictionary = []
    counter = 0
    for a in listobj:
        counter += 1
        dictionary = {counter: task_09_utility.get_data(listobj)}

def merge_data(dictobj):


    """
    Merges and sorts the dictionary"""
    
    dictionary = {}
    for a, b in dictobj.iteritems():
        key = b.values()['day']['hour']
        if key in dictionary:
            key.values()[idctobj['clock']][dictobj['value_avg']]
        else: key.values()[0]
    sortedlist = task_09_utility.sort_dict()
    return sortedlist
