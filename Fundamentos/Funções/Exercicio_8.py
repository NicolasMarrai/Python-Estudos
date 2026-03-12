"""Crie uma função chamada maior_numero(*numeros) que:
receba vários números
retorne o maior número entre eles
Exemplo:
maior_numero(3, 8, 2, 15, 7)
Saída: 15"""

def maior_numero(*numeros):
    maior = numeros[0]
    for n in numeros:
        if (n > maior):
            maior = n
    return maior

print(maior_numero(5, 24, 32, 0))