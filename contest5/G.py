import random

hash_dict = {}
for c in range(1, 10 ** 5 + 1):
    hash_dict[c] = random.randint(1, 2 ** 64)


def string_hash(s):
    global hash_dict
    hash_list = [0]
    for e in s:
        hash_list.append(hash_list[-1] + hash_dict[int(e)])

    return hash_list


def substring_hash(hash, l, r): # 0-индексация
    return hash[r + 1] - hash[l]


n = int(input())
a = input().strip().split()
m = int(input())
b = input().strip().split()

hash_a = string_hash(a)
hash_b = string_hash(b)
max_len = 0

for length in range(1, min(n, m) + 1):
    hashes = set()
    for i in range(n - length + 1):
        hash = substring_hash(hash_a, i, i + length - 1)
        hashes.add(hash)
    for i in range(m - length + 1):
        hash = substring_hash(hash_b, i, i + length - 1)
        if hash in hashes:
            max_len = length
            break

print(max_len)
