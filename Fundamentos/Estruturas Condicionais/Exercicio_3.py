login = input("Usuário: ")
senha = int(input("Senha: "))

if (login != "admin" and senha == 1234):
    print("Usuário não encontrado!")
elif (login == "admin" and senha != 1234):
    print("Senha incorreta!")
else:
    print("Acesso permitido!")