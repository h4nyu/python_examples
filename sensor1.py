import sys
import time

sensorValue = 0.0
while True:
    sensorValue += 0.1
    sys.stdout.write("{0}\n".format(sensorValue))
    sys.stdout.flush()
    time.sleep(0.3)
