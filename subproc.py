
# -*- coding: utf-8 -*-

import subprocess
import time

if __name__ == "__main__":
    start_time = time.time()
    procs = []
    for i in range(10):
        proc = subprocess.Popen(['sleep', str(1)])
        procs.append(proc)

    for proc in procs:
        print(proc.wait())

    end_time = time.time()

    print(round(end_time - start_time, 2))
