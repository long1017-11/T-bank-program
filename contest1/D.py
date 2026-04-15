def equation(x):
    return x ** 2 + (x + 1) ** 0.5


c = float(input())
l = 0
r = c ** 0.5
res = 0

while r - l >= 0.1 ** 7:
    res = (l + r) / 2
    curr_c = equation(res)
    if curr_c > c:
        r = res
    else:
        l = res

print(round(res, 6))
