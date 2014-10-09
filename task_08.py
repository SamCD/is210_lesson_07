#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data import FRUIT
def get_cost_per_item(shoplist):
    cost = {a: (b * a)} for a, b in iteritems(shoplist) if a is in FRUIT
    return cost
def get_total_cost(shoplist):
    total = sum(cost) for a, b in get_cost_per_item(shoplist)
    return total
