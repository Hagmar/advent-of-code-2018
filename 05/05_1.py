import sys
from collections import defaultdict, Counter
from functools import reduce

line = sys.stdin.read().strip()
x = zip(line, line[1:])

i = 0
while i < len(line)-1:
    if line[i].upper() == line[i+1].upper() and line[i] != line[i+1]:
        line = line[:i] + line[i+2:]
        i = 0
    else:
        i += 1


print(len(line))
