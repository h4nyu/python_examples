import sys
import time
while True:
    s = raw_input()
    print "{}\n".format(s)
    time.sleep(2)
    sys.stdout.flush()
