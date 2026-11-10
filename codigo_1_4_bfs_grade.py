from collections import deque

n, m = map(int, input().split())
g = [input() for _ in range(n)]
for i in range(n):
    for j in range(m):
        if g[i][j] == 'S':
            sr, sc = i, j
        if g[i][j] == 'T':
            tr, tc = i, j
d = [[-1] * m for _ in range(n)]
d[sr][sc] = 0
fila = deque([(sr, sc)])
while fila:
    r, c = fila.popleft()
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if not (0 <= nr < n and 0 <= nc < m):
            continue
        if g[nr][nc] == '#' or d[nr][nc] != -1:
            continue
        d[nr][nc] = d[r][c] + 1
        fila.append((nr, nc))
print(d[tr][tc])   # -1 se T for inalcançável
