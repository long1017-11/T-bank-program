n = int(input())
balls = list(map(int, input().split()))
stack = []
del_cnt = 0

for i in range(n):
    stack.append(balls[i])
    if len(stack) >= 3 and stack[-1] == stack[-2] == stack[-3] and (i == n - 1 or balls[i + 1] != stack[-1]):
        to_delete = stack[-1]
        while len(stack) > 0 and to_delete == stack[-1]:
            stack.pop()
            del_cnt += 1

print(del_cnt)
