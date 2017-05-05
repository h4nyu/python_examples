#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time


def countdown(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    COUNT = 100000000
    start = time.clock()
    t1 = threading.Thread(target=countdown, args=(COUNT // 2, ))
    t2 = threading.Thread(target=countdown, args=(COUNT // 2, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.clock() - start
    print(end)
