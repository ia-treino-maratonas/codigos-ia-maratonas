import sys

dados = sys.stdin.buffer.read().split()
n, k = int(dados[0]), int(dados[1])
c = list(map(int, dados[2:2 + n]))

def pedacos(L):           # quantos pedaços de tamanho L
    return sum(x // L for x in c)

lo, hi = 0, max(c)        # resposta está em [lo, hi]
while lo < hi:
    meio = (lo + hi + 1) // 2
    if pedacos(meio) >= k:
        lo = meio         # funciona: tente maior
    else:
        hi = meio - 1     # não funciona: tente menor
print(lo)                 # 0 se for impossível
