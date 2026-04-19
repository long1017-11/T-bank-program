m = int(input().strip())

graph = {}
for _ in range(m):
    u, v = input().strip().split(' -> ')
    graph.setdefault(u, []).append(v)

start = input().strip()
end = input().strip()


def find_shortest_path(graph, start, end):
    from collections import deque
    queue = deque()
    visited = {start}
    queue.append((start, 0))

    while queue:
        node, length = queue.popleft()
        if node == end:
            return length

        for next in graph.get(node, []):
            if next in visited: continue
            queue.append((next, length + 1))
            visited.add(next)

    return -1


print(find_shortest_path(graph, start, end))
