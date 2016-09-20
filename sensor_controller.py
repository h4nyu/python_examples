from subprocess import Popen, PIPE
import matplotlib.pyplot as plt
import time
from fcntl import fcntl, F_GETFL, F_SETFL
from os import O_NONBLOCK, read


class Senser(object):

    def __init__(self, name):
        self.proc = Popen(['python', name],
                          stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=False)
        flags = fcntl(self.proc.stdout, F_GETFL)  # get current p.stdout flags
        fcntl(self.proc.stdout, F_SETFL, flags | O_NONBLOCK)
        self.value = 0

    def getValue(self):
        try:
            value = read(self.proc.stdout.fileno(), 1024)
        except OSError:
            pass
        else:
            self.value = value
        return self.value


sensers = []
senser = Senser('./shell.py')
sensers.append(senser)
senser = Senser('./stdout.py')
sensers.append(senser)
# run the shell as a subprocess:

start_time = time.time()
senser0=[]
senser1=[]

for i in range(30):
    for senser in sensers:
        senser.proc.stdin.write('{0}\n'.format(senser.proc.pid))

    time.sleep(0.1)
    nowtime = round(time.time() - start_time, 2)
    print(nowtime)

    senser0.append(sensers[0].getValue())
    senser1.append(sensers[1].getValue())

plt.plot(senser0)
plt.plot(senser1)
plt.show()


