import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    arr = [0] * n
    for i in range(n):
        arr[i] = int(next(it))
    
    
    size = 1
    while size < n:
        size <<= 1
    tree = [0] * (2 * size)
    
    
    for i in range(n):
        tree[size + i] = arr[i]
    for i in range(size - 1, 0, -1):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]
    
    out_lines = []
    
    for _ in range(m):
        op = int(next(it))
        if op == 1:
            idx = int(next(it))
            pos = size + idx
            tree[pos] ^= 1  # flip
            pos >>= 1
            while pos:
                tree[pos] = tree[pos << 1] + tree[pos << 1 | 1]
                pos >>= 1
        else:  # op == 2
            k = int(next(it))
            pos = 1
            while pos < size:
                if tree[pos << 1] > k:
                    pos = pos << 1
                else:
                    k -= tree[pos << 1]
                    pos = pos << 1 | 1
            out_lines.append(str(pos - size))
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
