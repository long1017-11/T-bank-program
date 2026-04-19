import sys

sys.setrecursionlimit(10 ** 6)


def has_cycle(graph, n):
    color = {i: 'white' for i in range(1, n + 1)}

    def dfs(node):
        color[node] = 'grey'
        for neighbor in graph[node]:
            if color[neighbor] == 'white' and dfs(neighbor):
                return True
            elif color[neighbor] == 'grey':
                return True

        color[node] = 'black'
        return False

    for i in range(1, n + 1):
        if color[i] == 'white' and dfs(i):
            return True

    return False


n, m = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

print(1 if has_cycle(graph, n) else 0)
