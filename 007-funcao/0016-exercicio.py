import os
os.system('cls' if os.name == 'nt' else 'clear')

def inflacao(preco_produto):
    if preco_produto < 100:
        resultado = preco_produto + (preco_produto * 0.10)
        return resultado
    else:
        preco_produto >= 100
        resultado = preco_produto + (preco_produto * 0.20)
        return resultado

preco_produto = int(input("Digite o preço do produto: R$ "))
resultado = inflacao(preco_produto)

print(f'Preço do produto sem descontos: R$ {preco_produto}\nCom descontos: R$ {resultado}')