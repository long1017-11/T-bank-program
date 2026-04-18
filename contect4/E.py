def can_split_array(array, sum, k):
    curr_sum = 0
    count = 1

    for a in array:
        if curr_sum + a <= sum:
            curr_sum += a
        else:
            curr_sum = a
            count += 1
            if count > k: return False

    return True


def binary_search(array, k):
    left, right = max(array), sum(array)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_split_array(array, mid, k):
            right = mid - 1
            result = mid
        else:
            left = mid + 1

    return result


n, k = map(int, input().split())
array = list(map(int, input().split()))

print(binary_search(array, k))
