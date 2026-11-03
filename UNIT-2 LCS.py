s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

m = len(s1)
n = len(s2)

dp = [[0] * (n + 1) for i in range(m + 1)]

ans = 0

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
            ans = max(ans, dp[i][j])
        else:
            dp[i][j] = 0

print("Longest Common Substring Length:", ans)
