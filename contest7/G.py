s = input().strip()
n = len(s)

dp = [[''] * n for _ in range(n)]

for length in range(2, n + 1):
    for l in range(n - length + 1):
        r = l + length - 1

        if ((s[l] == '(' and s[r] == ')') or
            (s[l] == '[' and s[r] == ']') or
            (s[l] == '{' and s[r] == '}')):
            dp[l][r] = s[l] + dp[l + 1][r - 1] + s[r]

        for k in range(l, r):
            if len(dp[l][r]) < len(dp[l][k]) + len(dp[k + 1][r]):
                dp[l][r] = dp[l][k] + dp[k + 1][r]

print(dp[0][n - 1])
