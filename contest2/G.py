from collections import deque

n = int(input())
start = deque()
end = deque()

for _ in range(n):
    t = input().split()
    if t[0] == '+':
        start.appendleft(t[1])
    elif t[0] == '*':
        start.append(t[1])
    else:
        print(end.pop())

    if len(end) < len(start):
        end.appendleft(start.pop())
