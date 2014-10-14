#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Does useful calculations on a shopping list"""

from data import FRUIT
def get_cost_per_item(shoplist):

    """

    Gets cost for each item, given a quantity"""

    cost = {a: FRUIT[a] * b for a, b in shoplist.iteritems() if a in FRUIT}
    return cost

def get_total_cost(shoplist):

    """

    Sums up the total cost of the list"""

    total = 0
    total = sum(get_cost_per_item(shoplist).values())
    return total
