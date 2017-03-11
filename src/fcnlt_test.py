from fcntl import fcntl, F_GETFL, F_SETFL
import sys

import sys
import subprocess

print(sys.stdin.fileno())
print(sys.stdout.fileno())
print(sys.stderr.fileno())

proc = subprocess.Popen('ls', stdout=subprocess.PIPE)

print(proc.stdout.fileno())


print(sys.stdin)
print(sys.stdout)
print(sys.stderr)
