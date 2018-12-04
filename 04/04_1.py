import sys
from collections import defaultdict

lines = sys.stdin.readlines()
sleeps = defaultdict(lambda: defaultdict(int))
total_sleep = defaultdict(int)

guard = None
curr_hour = 0
curr_minute = 0
for line in lines:
    _, time, *rest = line.strip().split()
    hour = int(time[:2])
    minute = int(time[3:-1])

    if 'Guard' in rest:
        guard = int(rest[1][1:])
        curr_hour, curr_minute = 0, minute
    elif 'falls' in rest:
        curr_minute = minute
    elif 'wakes' in rest:
        s = sleeps[guard]
        for m in range(curr_minute, minute):
            s[m] += 1
        total_sleep[guard] += minute-curr_minute

s_guard = max(total_sleep.items(), key=lambda x: x[1])[0]
s_minute = max(sleeps[s_guard].items(), key=lambda x: x[1])[0]

print(s_guard * s_minute)
