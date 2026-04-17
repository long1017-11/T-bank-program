import sys

sys.setrecursionlimit(10000)


def find_lca(parents, u, v, u_nodes=None, v_nodes=None):
    if not u_nodes and not v_nodes:
        u_nodes = set()
        v_nodes = set()

    u_nodes.add(u)
    v_nodes.add(v)

    if v in u_nodes:
        return v

    if u in v_nodes:
        return u

    if u == 0:
        return find_lca(parents, parents[u], parents[v - 1], u_nodes, v_nodes)
    if v == 0:
        return find_lca(parents, parents[u - 1], parents[v], u_nodes, v_nodes)

    return find_lca(parents, parents[u - 1], parents[v - 1], u_nodes, v_nodes)


n = int(input())
parents = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    u, v = map(int, input().split())
    print(find_lca(parents, u, v))
