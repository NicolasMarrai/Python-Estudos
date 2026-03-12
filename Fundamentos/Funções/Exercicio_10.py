"""Crie uma função chamada criar_usuario(**dados).
Ela deve:
imprimir "Usuário criado com sucesso"
depois mostrar todos os dados recebidos.
Exemplo:
criar_usuario(nome="Lucas", email="lucas@email.com", idade=22)"""

def criar_usuario(**dados):
    print("Usuário criado com sucesso")
    for dados, info in dados.items():
        print(dados, ":", info)

criar_usuario(nome="Lucas", email="lucas@email.com", idade=22)