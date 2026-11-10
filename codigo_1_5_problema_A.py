import sys
from bisect import bisect_right

dados = sys.stdin.buffer.read().split()  # lê tudo de uma vez
n, q = int(dados[0]), int(dados[1])
h = sorted(map(int, dados[2:2 + n]))      # O(N log N)
saida = []
for x in dados[2 + n:2 + n + q]:
    # quantas alturas são <= x
    saida.append(bisect_right(h, int(x)))  # O(log N)
print('\n'.join(map(str, saida)))
