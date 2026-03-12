"""Exercício 4 — Um pouco mais difícil
Crie uma função chamada media(n1, n2, n3) que:
receba 3 notas
calcule a média
retorne o valor da média
Depois verifique:
média ≥ 7 → "Aprovado"
média ≥ 5 → "Recuperação"
menor que 5 → "Reprovado"""

def media(n1, n2, n3):
    return (n1 + n2 + n3)/3

resultado = media(1, 1, 1)

if(resultado < 5):
    print("Reprovado")
elif (resultado < 7):
    print("Recuperação")
else:
    print("Aprovado")