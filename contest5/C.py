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


def substring_hash(hash, l, r): # 0-индексация
    return ((hash[r + 1] - hash[l] * k_powers[r - l + 1]) % m + m) % m


a = input().strip()
b = input().strip()

hash_a = string_hash(a)
hash_b = string_hash(b + b)
hashes_anagrams = set()
cnt = 0

for i in range(len(b) + 1):
    hashes_anagrams.add(substring_hash(hash_b, i, i + len(b) - 1))

for i in range(len(a) - len(b) + 1):
    hash = substring_hash(hash_a, i, i + len(b) - 1)
    if hash in hashes_anagrams:
        cnt += 1

print(cnt)
