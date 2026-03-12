"""Exercício 9 — Básico
Crie uma função chamada mostrar_informacoes(**dados).
A função deve imprimir todas as informações recebidas.
Exemplo de chamada:
mostrar_informacoes(nome="Ana", idade=20, cidade="Uberaba")
Saída esperada:
nome : Ana
idade : 20
cidade : Uberaba"""

def mostrar_informacoes(**dados):
    for info, valor in dados.items():
        print(info, ":", valor)
mostrar_informacoes(nome="Ana", idade=20, cidade="Uberaba")