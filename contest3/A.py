import sys

sys.setrecursionlimit(200000)


def dfs(v, parent, tree, depths):
    for u in tree[v]:
        if u == parent: continue
        depths[u] = depths[v] + 1
        dfs(u, v, tree, depths)


def find_height_and_diameter(tree, n):
    depths = [-1] * n
    depths[0] = 0
    dfs(0, -1, tree, depths)

    height = max(depths)
    farthest_node = depths.index(height)

    diameters = [-1] * n
    diameters[farthest_node] = 0
    dfs(farthest_node, -1, tree, diameters)

    diameter = max(diameters)

    return height, diameter, depths


n = int(input())
parents = list(map(int, input().split()))

tree = [[] for _ in range(n)]
for i, p in enumerate(parents, 1):
    tree[p].append(i)
    tree[i].append(p)

height, diameter, depths = find_height_and_diameter(tree, n)
print(height, diameter)
print(' '.join(map(str, depths)))
