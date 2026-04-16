import sys
from collections import deque


deq = deque()
id_map = {}
cnt, buy_cnt = 0, 0

# буферизированный ввод для оптимизации
file = sys.stdin.readlines()
n = int(file[0].rstrip('\n'))
for i in range(1, n + 1):
    t = file[i].rstrip('\n').split()
    if t[0] == '1':
        deq.appendleft(t[1])
        id_map[t[1]] = cnt
        cnt += 1
    elif t[0] == '2':
        deq.pop()
        buy_cnt += 1
    elif t[0] == '3':
        deq.popleft()
        cnt -= 1
    elif t[0] == '4':
        print(id_map[t[1]] - buy_cnt)
    else:
        print(deq[-1])
