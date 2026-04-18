import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx]); idx += 1
    
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(data[idx]); idx += 1
    
    m = int(data[idx]); idx += 1
    
    prefix_sum = [0] * (n + 1)
    prefix_xor = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + a[i]
        prefix_xor[i] = prefix_xor[i - 1] ^ a[i]
    
    out_lines = []
    for _ in range(m):
        q_type = int(data[idx]); idx += 1
        l = int(data[idx]); idx += 1
        r = int(data[idx]); idx += 1
        
        if q_type == 1:
            out_lines.append(str(prefix_sum[r] - prefix_sum[l - 1]))
        else:
            out_lines.append(str(prefix_xor[r] ^ prefix_xor[l - 1]))
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
