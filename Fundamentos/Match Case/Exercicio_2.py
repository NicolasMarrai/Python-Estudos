"""🟡 Exercício 8 — Médio
Crie um programa que peça ao usuário um número de 1 a 5 e mostre o nome do dia da semana.
Exemplo:
1 -> Domingo
2 -> Segunda
3 -> Terça
...
Use match case."""

numero = int(input("Digite um número: (1 a 7): "))

match numero:
    case 1:
        print(numero, " -> ", "Domingo")
    case 2:
        print(numero, " -> ", "Segunda")
    case 3:
        print(numero, " -> ", "Terça")
    case 4:
        print(numero, " -> ", "Quarta")
    case 5:
        print(numero, " -> ", "Quinta")
    case 6:
        print(numero, " -> ", "Sexta")
    case 7:
        print(numero, " -> ", "Sábado")
    case _:
        print("Número incorreto")