import sys
import time
import numpy as np

while True:
    sensorValue = np.random.rand()
    sys.stdout.write("{0}\n".format(sensorValue))
    sys.stdout.flush()
    time.sleep(1)
