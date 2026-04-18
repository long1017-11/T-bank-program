def z_function(s):
    zf = len(s) * [0]
    l, r = 0, 0

    for i in range(1, len(s)):
        zf[i] = max(0, min(r - i, zf[i - l]))
        while i + zf[i] < len(s) and s[zf[i]] == s[i + zf[i]]:
            zf[i] += 1
        if i + zf[i] > r:
            l = i
            r = i + zf[i]

    return zf


p = input().strip()
t = input().strip()

pt = f'{p}${t}'
zf = z_function(pt)
pt_reversed = f'{p[::-1]}#{t[::-1]}'
zf_reversed = z_function(pt_reversed)
result = []

for i in range(len(p) + 1, len(pt) - len(p) + 1):
    if zf[i] == len(p) or zf[i] + zf_reversed[len(pt) - i + 1] == len(p) - 1:
        result.append(i - len(p))

print(len(result))
print(' '.join(map(str, result)))
