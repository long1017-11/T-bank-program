n = int(input())
stairs = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[1] = stairs[0]

for i in range(2, n + 1):
    dp[i] = min(dp[i - 1], dp[i - 2]) + stairs[i - 1]

print(dp[n])
