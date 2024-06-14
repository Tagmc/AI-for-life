def levenshtein_distance(token1, token2):
    m, n = len(token1), len(token2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for i in range(n + 1):
        dp[0][i] = i
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if token1[i - 1] == token2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] +
                           1, dp[i - 1][j - 1] + cost)
    return dp[m][n]


if __name__ == "__main__":
    print(levenshtein_distance("hola", "hello"))
