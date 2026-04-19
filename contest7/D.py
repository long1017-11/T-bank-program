def horse_shortest_path(n, x1, y1, x2, y2):
    from collections import deque
    moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, -1), (-2, 1)]
    visited = set()
    queue = deque()
    queue.append((x1, y1, []))

    while queue:
        x, y, path = queue.popleft()
        new_path = path + [(x, y)]
        if (x, y) == (x2, y2):
            return len(new_path) - 1, new_path

        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if 1 <= nx <= n and 1 <= ny <= n and not (nx, ny) in visited:
                queue.append((nx, ny, new_path))
                visited.add((nx, ny))


n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

k, path = horse_shortest_path(n, x1, y1, x2, y2)

print(k)
for p in path:
    print(p[0], p[1])
