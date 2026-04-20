import sys
import bisect

MOD = 10**9 + 7

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))
    
    
    unique_vals = sorted(set(arr))
    val_to_idx = {v: i + 1 for i, v in enumerate(unique_vals)} 
    comp_arr = [val_to_idx[x] for x in arr]
    
    size = 1
    while size <= len(unique_vals):
        size <<= 1
    
    
    max_len_tree = [0] * (2 * size)
    count_tree = [0] * (2 * size)
    
    def merge(node):
        left = node << 1
        right = node << 1 | 1
        if max_len_tree[left] > max_len_tree[right]:
            max_len_tree[node] = max_len_tree[left]
            count_tree[node] = count_tree[left]
        elif max_len_tree[right] > max_len_tree[left]:
            max_len_tree[node] = max_len_tree[right]
            count_tree[node] = count_tree[right]
        else:
            max_len_tree[node] = max_len_tree[left]
            count_tree[node] = (count_tree[left] + count_tree[right]) % MOD
    
    def query(l, r):
        """Query over [l, r) range, returns (max_len, count)"""
        res_max = 0
        res_cnt = 0
        l += size
        r += size
        while l < r:
            if l & 1:
                if max_len_tree[l] > res_max:
                    res_max = max_len_tree[l]
                    res_cnt = count_tree[l]
                elif max_len_tree[l] == res_max:
                    res_cnt = (res_cnt + count_tree[l]) % MOD
                l += 1
            if r & 1:
                r -= 1
                if max_len_tree[r] > res_max:
                    res_max = max_len_tree[r]
                    res_cnt = count_tree[r]
                elif max_len_tree[r] == res_max:
                    res_cnt = (res_cnt + count_tree[r]) % MOD
            l >>= 1
            r >>= 1
        return res_max, res_cnt
    
    def update(pos, max_len, cnt):
        pos += size
        if max_len_tree[pos] < max_len:
            max_len_tree[pos] = max_len
            count_tree[pos] = cnt
        elif max_len_tree[pos] == max_len:
            count_tree[pos] = (count_tree[pos] + cnt) % MOD
        pos >>= 1
        while pos:
            merge(pos)
            pos >>= 1
    
    for val in comp_arr:
        best_len, best_cnt = query(0, val)  # query values < current
        if best_len == 0:
            update(val, 1, 1)
        else:
            update(val, best_len + 1, best_cnt)
    
    total_len, total_cnt = query(0, len(unique_vals) + 1)
    print(total_cnt % MOD)

if __name__ == "__main__":
    solve()
