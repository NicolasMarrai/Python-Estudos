"""Exercício 6 — Um pouco mais difícil
Crie uma função chamada calcular_desconto(valor, desconto=10).
Ela deve:
calcular o valor com desconto
retornar o valor final
Exemplo:
calcular_desconto(100)
Desconto padrão de 10%.
Teste também:
calcular_desconto(100, 20)"""

def calcular_desconto(valor, desconto = 10):
    resultado = valor - (valor * desconto) / 100
    print(resultado)

calcular_desconto(100, 20)