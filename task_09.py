#!/usr/bin/env python
# -*- coding: utf-8 -*-

import task_09_utility.py
DATA_FILES = ['task_09_data/router_01.csv', 'task_09_data/router_02.csv',
              'task_09_data/router_03.csv']
def load_data(listobj):
    dictionary = []
    counter = 0
    for a, b in iteritems(listobj):
        counter += 1
        
