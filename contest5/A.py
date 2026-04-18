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


def substring_hash(hash, l, r): # 1-индексация
    return ((hash[r] - hash[l - 1] * k_powers[r - l + 1]) % m + m) % m


s = input()
q = int(input())

hash_s = string_hash(s)

for _ in range(q):
    a, b, c, d = map(int, input().split())
    if substring_hash(hash_s, a, b) == substring_hash(hash_s, c, d):
        print('Yes')
    else:
        print('No')
