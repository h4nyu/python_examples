#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
import random


def worker(number):
    sleep_time = random.randrange(1, 10)
    time.sleep(sleep_time)
    print("I am worker {}, I slept for {}, seconds".format(number, sleep_time))

for i in range(5):
    t = threading.Thread(target=worker, args=(i, ))
    t.start()

print("All Threads are queued, let's see when they finish!")
