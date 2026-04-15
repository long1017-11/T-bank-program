def equation(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d


def find_root(a, b, c, d):
    if d == 0: return 0

    l = -1111
    r = 1111
    res = 0

    if a > 0:
        while r - l >= 0.1 ** 5:
            res = (l + r) / 2
            ans = equation(a, b, c, d, res)
            if ans == 0:
                break
            elif ans > 0:
                r = res
            else:
                l = res
    else:
        while r - l >= 0.1 ** 5:
            res = (l + r) / 2
            ans = equation(a, b, c, d, res)
            if ans == 0:
                break
            elif ans > 0:
                l = res
            else:
                r = res

    return round(res, 4)


a, b, c, d = map(int, input().split())
print(find_root(a, b, c, d))
