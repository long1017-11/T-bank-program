n, m, k = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(m):
        prefix_sum[i + 1][j + 1] = prefix_sum[i][j + 1] + prefix_sum[i + 1][j] + matrix[i][j] - prefix_sum[i][j]

for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    sum_2d = prefix_sum[y2][x2] - prefix_sum[y2][x1 - 1] - prefix_sum[y1 - 1][x2] + prefix_sum[y1 - 1][x1 - 1]
    print(sum_2d)
