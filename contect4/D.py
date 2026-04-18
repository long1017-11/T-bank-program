def count_less_equal(x, n):
    count = 0
    for i in range(1, n + 1):
        count += min(x // i, n)

    return count


def binary_search(n, k):
    left, right = 1, n * n
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if count_less_equal(mid, n) >= k:
            right = mid - 1
            result = mid
        else:
            left = mid + 1

    return result


n, k = map(int, input().split())
print(binary_search(n, k))
