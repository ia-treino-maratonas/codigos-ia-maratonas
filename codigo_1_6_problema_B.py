import sys
from bisect import bisect_left, bisect_right

dados = sys.stdin.buffer.read().split()
n, q = int(dados[0]), int(dados[1])
p = sorted(map(int, dados[2:2 + n]))
saida = []
pos = 2 + n
for _ in range(q):
    a, b = int(dados[pos]), int(dados[pos + 1])
    pos += 2
    ini = bisect_left(p, a)    # primeiro valor >= a
    fim = bisect_right(p, b)   # primeiro valor >  b
    saida.append(fim - ini)
print('\n'.join(map(str, saida)))
