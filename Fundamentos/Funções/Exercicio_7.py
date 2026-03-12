"""Crie uma função chamada somar_numeros(*numeros) que:
receba vários números
retorne a soma de todos eles.
Exemplo:
somar_numeros(1,2,3,4)
Resultado esperado: 10"""

def somar_numeros(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma
print(somar_numeros(1, 2, 3, 4))
