def count_palindromes(s):
    odd = len(s) * [1]
    even = (len(s) - 1) * [0]

    l, r = 0, 0
    for i in range(1, len(s)):
        if i < r:
            odd[i] = min(r - i + 1, odd[l + r - i])
        while i - odd[i] >= 0 and i + odd[i] < len(s) and s[i - odd[i]] == s[i + odd[i]]:
            odd[i] += 1
        if i + odd[i] - 1 > r:
            l = i - odd[i] + 1
            r = i + odd[i] - 1

    l, r = 0, 0
    for i in range(0, len(s) - 1):
        if i < r:
            even[i] = min(r - i, even[l + r - i - 1])
        while i - even[i] >= 0 and i + even[i] + 1 < len(s) and s[i - even[i]] == s[i + even[i] + 1]:
            even[i] += 1
        if i + even[i] > r:
            l = i - even[i] + 1
            r = i + even[i]

    return sum(odd) + sum(even)


s = input().strip()
print(count_palindromes(s))
