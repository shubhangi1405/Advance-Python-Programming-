#BOTTOM-UP APPROACH

n = int(input("Enter number of items: "))

wt = list(map(int, input("Enter weights: ").split()))
val = list(map(int, input("Enter values: ").split()))

W = int(input("Enter capacity: "))

dp = [[0] * (W + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for w in range(W + 1):
        if wt[i-1] <= w:
            dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]

print("Maximum Value:", dp[n][W])

#TOP-DOWN APPROACH
n = int(input("Enter number of items: "))

wt = list(map(int, input("Enter weights: ").split()))
val = list(map(int, input("Enter values: ").split()))

W = int(input("Enter capacity: "))

dp = [[-1] * (W + 1) for i in range(n + 1)]

def knapsack(n, W):
    if n == 0 or W == 0:
        return 0

    if dp[n][W] != -1:
        return dp[n][W]

    if wt[n-1] <= W:
        dp[n][W] = max(
            val[n-1] + knapsack(n-1, W-wt[n-1]),
            knapsack(n-1, W)
        )
    else:
        dp[n][W] = knapsack(n-1, W)

    return dp[n][W]

print("Maximum Value:", knapsack(n, W))
