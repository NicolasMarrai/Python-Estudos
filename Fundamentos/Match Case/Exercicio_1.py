"""🟢 Exercício 7 — Fácil
Crie um programa que peça ao usuário um comando:
iniciar
parar
pausar
Use match case para imprimir uma mensagem diferente para cada comando."""

comando = input("Digite um comando: ")

match comando:
    case "iniciar":
        print("Comando iniciado!")
    case "parar":
        print("Comando parado!")
    case "pausar":
        print("Comando pausado!")
    case _:
        print("Comando não identificado!")