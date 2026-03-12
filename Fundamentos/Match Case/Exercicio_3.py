"""🔴 Exercício 9 — Difícil
Crie um menu simples:
1 - Ver saldo
2 - Depositar
3 - Sacar
4 - Sair
Peça para o usuário escolher uma opção e use match case para responder."""

print("Menu:")
print("1 - Ver saldo")
print("2 - Depositar")
print("3 - Sacar")
print("4 - Sair")

x = int(input("Digite a opção: "))

match x:
    case 1:
        print("Saldo: R$", 1500.00)
    case 2:
        print("Depositar: ")
    case 3:
        print("Sacar: ")
    case 4:
        print("Saindo...")
    case _:
        print("Opção inválida")