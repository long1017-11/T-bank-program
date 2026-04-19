n, m = map(int, input().split())

dp = [[0] * (m + 3) for _ in range(n + 3)]
dp[2][2] = 1

st_x, st_j = 2, 2
while st_x < n + 2:
    x, y = st_x, st_j
    while y > 1 and x < n + 2:
        dp[x][y] += dp[x - 2][y - 1] + dp[x - 2][y + 1] + dp[x - 1][y - 2] + dp[x + 1][y - 2]
        x += 1
        y -= 1
    if st_j < m + 1:
        st_j += 1
    else:
        st_x += 1

print(dp[n + 1][m + 1])
