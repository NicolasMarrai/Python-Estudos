"""🟡 Exercício 14 — Médio
Crie um sistema que peça uma senha.
Senha correta: python123
Enquanto a senha estiver errada, o programa deve pedir novamente.
Quando acertar: Acesso liberado"""

senha = ""

while (senha != "python123"):
    print("Senha Incorreta!")
    senha = input("Digite a senha: ")
print("Acesso Lierado")