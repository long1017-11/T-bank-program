n = int(input())
a = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + a[i]

stack = []
left = [-1] * n
for i in range(n):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    if stack:
        left[i] = stack[-1]
    stack.append(i)

stack = []
right = [n] * n
for i in range(n - 1, -1, -1):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    if stack:
        right[i] = stack[-1]
    stack.append(i)

result = 0
for i in range(n):
    l, r = left[i] + 1, right[i] - 1
    segment = (prefix_sum[r + 1] - prefix_sum[l]) * a[i]
    result = max(result, segment)

print(result)
