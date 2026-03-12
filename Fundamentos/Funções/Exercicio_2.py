"""Um pouco mais difícil
Crie uma função chamada tabuada(numero) que receba um número e imprima a tabuada de 1 a 10 desse número.
Exemplo:
tabuada(5)
Saída esperada:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50"""

def tabuada(numero):
    for n in range(1, 11):
        resultado = n * numero
        print(numero, "*", n, " = ", resultado)

tabuada(5)