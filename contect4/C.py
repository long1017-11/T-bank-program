def can_place_cows(stalls, k, distance):
    last_position = stalls[0]
    count = 1

    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= distance:
            count += 1
            last_position = stalls[i]
            if count == k: return True

    return False


def binary_search(stalls, k):
    l, r = 1, stalls[-1] - stalls[0]
    result = 0

    while l <= r:
        m = (l + r) // 2
        if can_place_cows(stalls, k, m):
            l = m + 1
            result = m
        else:
            r = m - 1

    return result


n, k = map(int, input().split())
stalls = list(map(int, input().split()))

print(binary_search(stalls, k))
