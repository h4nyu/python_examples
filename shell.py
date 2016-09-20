import sys
import time
s = 0
while True:
    # s = raw_input()
    # print "{}\n".format(s)
    sys.stdout.write("{0}\n".format(s))
    sys.stdout.flush()
    time.sleep(1)
    s += 1000
