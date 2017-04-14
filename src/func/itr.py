#!/usr/bin/env python
# -*- coding: utf-8 -*-

line_list = ['  line 1\n', 'line 2  \n']

# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list)
print(stripped_iter)

# List comprehension -- returns list
stripped_list = [line.strip() for line in line_list]
print(stripped_list)
