m = 10 ** 9 + 7
k = 31
k_powers = [1]
for _ in range(10 ** 5):
    k_powers.append((k_powers[-1] * k) % m)


def string_hash(s):
    hash_list = [0]
    for i in range(len(s)):
        char_num = ord(s[i]) - ord('a') + 1
        hash_list.append((hash_list[-1] * k + char_num) % m)

    return hash_list


def substring_hash(hash, l, r):  # 0-индексация
    return ((hash[r + 1] - hash[l] * k_powers[r - l + 1]) % m + m) % m


def get_LCP(hash, l1, r1, l2, r2):
    r = min(r2 - l2 + 1, r1 - l1 + 1)
    l = 1
    result = 0
    while l <= r:
        m = l + (r - l) // 2
        if substring_hash(hash, l1, l1 + m - 1) == substring_hash(hash, l2, l2 + m - 1):
            result = m
            l = m + 1
        else:
            r = m - 1

    return result


def substring_comparator(str, hash, l1, r1, l2, r2):
    lcp = get_LCP(hash, l1, r1, l2, r2)
    r_f = l1 + lcp
    r_s = l2 + lcp
    return str[r_f] > str[r_s]


s = input().strip()
double_s = s + s
hash_s = string_hash(double_s)
best_l, best_r = 0, len(s) - 1

for i in range(1, len(s)):
    l, r = i, i + len(s) - 1
    if not substring_comparator(double_s, hash_s, l, r, best_l, best_r):
        best_l, best_r = l, r

print(double_s[best_l:best_r + 1])
