def z_function(s, t):
    result = ''
    cnt = 0
    str = f'{s}${t}'
    zf = len(str) * [0]
    l, r = 0, 0

    for i in range(1, len(str)):
        zf[i] = max(0, min(r - i, zf[i - l]))
        while i + zf[i] < len(str) and str[zf[i]] == str[i + zf[i]]:
            zf[i] += 1
        if i + zf[i] > r:
            l = i
            r = i + zf[i]
        if zf[i] == len(s):
            result += f'{i - len(s) - 1} '
            cnt += 1

    return cnt, result.rstrip()


t = input()
q = int(input())

for _ in range(q):
    s = input().strip()
    cnt, result = z_function(s, t)

    print(cnt) if cnt == 0 else print(f'{cnt} {result}')
