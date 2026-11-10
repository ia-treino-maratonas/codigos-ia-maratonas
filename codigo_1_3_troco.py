n, x = map(int, input().split())
c = list(map(int, input().split()))

INF = float('inf')

dp = [INF] * (x + 1)  # dp[v]: mín. de moedas p/ somar v
dp[0] = 0              # caso base
for v in range(1, x + 1):
    for m in c:
        if m <= v and dp[v - m] + 1 < dp[v]:
            dp[v] = dp[v - m] + 1   # transição
print(dp[x] if dp[x] != INF else -1)
