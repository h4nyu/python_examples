from subprocess import Popen, PIPE
from time import sleep
from fcntl import fcntl, F_GETFL, F_SETFL
from os import O_NONBLOCK, read


def get_lines(proc):
    line = proc.stdout.readline()
    if line:
        return line
if __name__ == '__main__':

    # run the shell as a subprocess:
    proc = Popen(['python', './shell.py'],
              stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=False)
# set the O_NONBLOCK flag of p.stdout file descriptor:
# issue command:
    sleep(10)
# get the output
    print(get_lines(proc))

