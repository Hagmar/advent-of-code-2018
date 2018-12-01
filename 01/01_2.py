import sys
import itertools

found = set()
n = 0
for l in itertools.cycle(sys.stdin.readlines()):
    x = int(l)
    n += x
    if n in found:
        print(n)
        break
    found.add(n)
