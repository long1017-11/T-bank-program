n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (m + 1) for _ in range(n + 1)]

max_side = 0
max_x, max_y = 0, 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if matrix[i - 1][j - 1] == 1:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            if dp[i][j] > max_side:
                max_side = dp[i][j]
                max_x = i - max_side + 1
                max_y = j - max_side + 1

print(max_side)
print(max_x, max_y)
