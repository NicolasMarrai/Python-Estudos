"""🔴 Exercício 6 — Difícil
Crie uma lista de números:
[10, 20, 30, 40, 50]
Use for + enumerate para mostrar:
Posição 0 -> 10
Posição 1 -> 20
Posição 2 -> 30
..."""

numeros = [10, 20, 30, 40, 50]

for indice, numero in enumerate(numeros):
    print("Posição ", indice, " -> ", numero)