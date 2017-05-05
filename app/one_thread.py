#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time


def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    COUNT = 100000000
    start = time.clock()
    countdown(COUNT)
    end = time.clock() - start
    print(end)
