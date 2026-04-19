first = input()
second = input()
n = len(first)
m = len(second)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1): dp[i][0] = i
for i in range(m + 1): dp[0][i] = i

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if first[i - 1] == second[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        if 1 < i and 1 < j and first[i - 1] == second[j - 2] and second[j - 1] == first[i - 2]:
            dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)

print(dp[n][m])
