import sys
import time
while True:
    s = raw_input("Enter command: ")
    print "You entered: {}".format(s)
    time.sleep(0.3)
    sys.stdout.flush()
