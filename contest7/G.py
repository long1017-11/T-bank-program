def floyd_algorithm(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    optimal_city = -1
    min_distance = float('inf')

    for i in range(n):
        curr_distance = max(graph[i])
        if curr_distance < min_distance:
            min_distance = curr_distance
            optimal_city = i + 1

    return optimal_city


n, m = map(int, input().split())

graph = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u - 1][v - 1] = w
    graph[v - 1][u - 1] = w

print(floyd_algorithm(graph, n))
