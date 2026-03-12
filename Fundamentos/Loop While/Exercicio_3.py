"""🔴 Exercício 15 — Difícil
Crie um programa que:
Peça números ao usuário.
Some todos os números digitados.
O programa só para quando o usuário digitar 0.
No final mostre: Soma total: X"""

x = ""
soma = 0

while (x != 0):
    x = int(input("Digite um número: "))
    soma += x
print("Soma: ", soma)