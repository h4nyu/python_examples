from subprocess import Popen, PIPE
import sys
import time
from fcntl import fcntl, F_GETFL, F_SETFL
from os import O_NONBLOCK, read


class Senser(object):

    def __init__(self, name):
        self.proc = Popen(['python', name],
                          stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=False , bufsize=32)
        flags = fcntl(self.proc.stdout, F_GETFL)  # get current p.stdout flags
        fcntl(self.proc.stdout, F_SETFL, flags | O_NONBLOCK)
        self.value = 0.0

    def getValue(self):
        try:
            # value = read(self.proc.stdout.fileno(), )
            value = float(self.proc.stdout.readline())
        except:
            pass
        else:
            self.value = value
        return self.value


sensers = []
senser = Senser('./shell.py')
sensers.append(senser)
senser = Senser('./distance_sensor.py')
sensers.append(senser)
# run the shell as a subprocess:

start_time = time.time()
senser0 = []
senser1 = []

# for i in range(50):
while True:

    time.sleep(0.1)
    nowtime = round(time.time() - start_time, 2)

    print('===============')
    print sensers[0].getValue()
    print sensers[1].getValue()

