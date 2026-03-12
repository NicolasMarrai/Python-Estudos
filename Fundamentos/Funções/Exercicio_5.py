"""Exercício 5 — Básico
Crie uma função chamada boas_vindas(nome="Visitante").
A função deve imprimir:
Bem-vindo, NOME
Teste:
boas_vindas()
boas_vindas("Carlos")"""

def boas_vindas(nome = "visitante"):
    print("Bem-vindo", nome)

boas_vindas()
boas_vindas("Nicolas")