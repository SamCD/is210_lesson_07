#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 07, Task 05"""


import data

SUPER_SIDEKICKS = {}
for HERO, HERO_DATA in data.SUPERHEROES.iteritems():
    SUPER_SIDEKICKS[HERO] = SUPER_SIDEKICKS.get(HERO_DATA['pet'])
