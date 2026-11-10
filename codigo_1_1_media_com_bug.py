n = int(input())
valores = list(map(int, input().split()))
soma = sum(valores)
print(int(soma / n))  # BUG: "/" gera um float
