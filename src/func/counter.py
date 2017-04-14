#!/usr/bin/env python
# -*- coding: utf-8 -*-


def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
# If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1


if __name__ == "__main__":
    it = counter(10)
    print(next(it))
    print(next(it))
