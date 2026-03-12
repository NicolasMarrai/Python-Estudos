"""Exercício 12 — Um pouco mais difícil
Crie uma função lambda que:
receba dois números
retorne o maior entre eles
Exemplo:
maior(10, 7)
Saída: 10"""

maior = lambda x, y: x if x > y else y

print(maior(10, 7))