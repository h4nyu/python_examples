import sys
from subprocess import PIPE, Popen
from threading import Thread

try:
    from Queue import Queue, Empty
except ImportError:
    from queue import Queue, Empty  # python 3.x


def enqueue_output(out, queue):
    time.sleep(0.1)
    for line in iter(out.readline()):
        queue.put(line)
    out.close()


p = Popen(['python', './stdout.py'], stdout=PIPE, bufsize=1)
q = Queue()
t = Thread(target=enqueue_output, args=(p.stdout, q))
t.daemon = True  # thread dies with the program
t.start()

# ... do other things here

# read line without blocking

try:
    line = q.get_nowait()  # or q.get(timeout=.1)
    print(line)
except Empty:
    print('no output yet')
