import sys
import time
s=0
while True:
    # s = raw_input()
    print "{}\n".format(s)
    time.sleep(1)
    sys.stdout.flush()
    s +=1000
