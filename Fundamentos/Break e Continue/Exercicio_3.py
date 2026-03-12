"""🔴 Exercício 12 — Difícil
Crie um programa que percorra números de 1 a 50.
Regras:
Se o número for múltiplo de 7, use continue
Se o número for maior que 40, use break
Imprima os outros números."""

for i in range(1, 50):
    if (i % 7 == 0):
        continue
    elif (i > 40):
        break
    print(i)