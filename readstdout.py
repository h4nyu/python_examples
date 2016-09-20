import subprocess
import time
proc = subprocess.Popen(['python', './stdout.py'], stdout=subprocess.PIPE)

print "ready"


while True:
    time.sleep(0.3)
    line = proc.stdout.read(1)
    if line:
        print(line)
    else:
        break

    queue.put(line)

