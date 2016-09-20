import sys
import time
while True:
    s = raw_input()
    # print "{}".format(s)
    sys.stdout.write("{0}".format(s))
    time.sleep(0.3)
    sys.stdout.flush()
