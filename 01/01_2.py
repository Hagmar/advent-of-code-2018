import sys

found = set()
n = 0
i = 0
lines = sys.stdin.readlines()
while True:
    x = int(lines[i])
    n += x
    if n in found:
        print(n)
        break
    found.add(n)
    i = (i+1) % len(lines)
