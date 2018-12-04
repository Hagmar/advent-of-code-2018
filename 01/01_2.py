import sys
import itertools

found = set()
n = 0
for l in itertools.cycle(sys.stdin.readlines()):
    n += int(l)
    if n in found:
        print(n)
        break
    found.add(n)
