def time_to_seconds(h, m, s):
    return h * 3600 + m * 60 + s


import sys

file = sys.stdin.readlines()

n = int(file[0].rstrip('\n'))
total_seconds = time_to_seconds(24, 0, 0)
events = []

for i in range(1, n + 1):
    h1, m1, s1, h2, m2, s2 = map(int, file[i].rstrip('\n').split())
    start = time_to_seconds(h1, m1, s1)
    end = time_to_seconds(h2, m2, s2)

    if start == end:
        events.append((0, 1))
        events.append((total_seconds, -1))
    else:
        if start < end:
            events.append((start, 1))
            events.append((end, -1))
        else:
            events.append((start, 1))
            events.append((total_seconds, -1))
            events.append((0, 1))
            events.append((end, -1))

events.sort(key=lambda x: (x[0], x[1]))
curr_cnt, last_time, total_time = 0, 0, 0

for time, e in events:
    if curr_cnt == n:
        total_time += time - last_time
    curr_cnt += e
    last_time = time

print(total_time)
