def binary_search_h(n, m):
    total_sum = (1 + n * m) / 2 * m * n
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        sum1 = (1 + mid * m) / 2 * mid * m
        if sum1 > total_sum - sum1:
            r = mid - 1
        else:
            l = mid + 1

    diff_l = abs(total_sum - (1 + l * m) / 2 * l * m * 2)
    diff_r = abs(total_sum - (1 + r * m) / 2 * r * m * 2)
    if diff_l < diff_r:
        return diff_l, l + 1
    else:
        return diff_r, r + 1


def binary_search_v(n, m):
    total_sum = (1 + n * m) / 2 * m * n
    l, r = 0, m - 1
    while l <= r:
        mid = (l + r) // 2
        sum1 = mid / 2 * (m * (n - 1) * n + n * (mid + 1))
        if sum1 > total_sum - sum1:
            r = mid - 1
        else:
            l = mid + 1

    diff_l = abs(total_sum - l / 2 * (m * (n - 1) * n + n * (l + 1)) * 2)
    diff_r = abs(total_sum - r / 2 * (m * (n - 1) * n + n * (r + 1)) * 2)
    if diff_l < diff_r:
        return diff_l, l + 1
    else:
        return diff_r, r + 1


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    diff_h, x_h = binary_search_h(n, m)
    diff_v, x_v = binary_search_v(n, m)
    if diff_v <= diff_h:
        print(f'V {x_v}')
    else:
        print(f'H {x_h}')
