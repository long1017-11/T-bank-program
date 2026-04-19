import bisect

n = int(input())
a = list(map(int, input().split()))

dp = [float('inf')] * (n + 1)
dp_pos = [0] * (n + 1)
path = [0] * n
max_len = 0
dp[0] = float('-inf')
dp_pos[0] = -1

for i in range(n):
    length = bisect.bisect_left(dp, a[i])
    dp[length], dp_pos[length]  = a[i], i
    path[i] = dp_pos[length - 1]
    max_len = max(length, max_len)

result = []
p = dp_pos[max_len]

while p != -1:
    result.append(a[p])
    p = path[p]

result.reverse()

print(max_len)
print(' '.join(map(str, result)))
