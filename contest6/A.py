from collections import deque

n, m = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

components = []
visited = set()
for i in range(1, n + 1):
    if i in visited: continue
    queue = deque()
    queue.append(i)
    curr_component = {i}
    while len(queue) > 0:
        node = queue.popleft()
        for next in graph[node]:
            if next in visited: continue
            queue.append(next)
            visited.add(next)
            curr_component.add(next)

    components.append(curr_component)

print(len(components))
for component in components:
    print(len(component))
    print(' '.join(map(str, sorted(component))))
