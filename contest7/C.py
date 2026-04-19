def check_topological_sort(edges, permutation):
    pos_map = {v: i for i, v in enumerate(permutation)}

    for u, v in edges:
        if pos_map[u] > pos_map[v]:
            return 'NO'

    return 'YES'


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
permutation = list(map(int, input().split()))

print(check_topological_sort(edges, permutation))
