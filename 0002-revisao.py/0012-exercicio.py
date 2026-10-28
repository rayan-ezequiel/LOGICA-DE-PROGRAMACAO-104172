# 1. Carrinho de Compras Interativo WHILE VETORESCONDICIONAL
# Crie um programa que receba o nome e o preço de vários produtos até que o usuário digite "fim".
#  Armazene os
# preços em um vetor, exiba o valor total acumulado, identifique o produto mais caro e aplique um 
# valor_com_desconto
# automático de 10% se o total ultrapassar R$ 100,00

import os
os.system('clear')

nome_do_produto = []
preco_do_produto = []

while True:
    
    nome = input('Digite o nome do produto: ')
    
    if nome != 'fim':
        nome_do_produto.append(nome)
    
        preco = float(input('Digite o preço do produto: R$ '))
        preco_do_produto.append(preco)

        total_acumulado = sum(preco_do_produto)
        produto_mais_caro = max(preco_do_produto)
        indice_mais_caro = preco_do_produto.index(produto_mais_caro)
        produto_correspodente = nome_do_produto[indice_mais_caro]

    
    elif nome == 'fim':
        if len(nome_do_produto) == 0 and len(preco_do_produto) == 0:
            print('Você não digitou nada ainda.')
            continue
            
        else:   
            if total_acumulado > 100:
                valor_com_desconto = total_acumulado - (total_acumulado * 0.10)
                os.system('clear')
                print('Vamos encerrar o programa e exibir os resultados.')
                print(f'O total acumulado foi de: R$ {total_acumulado} com um de 10% por ter passado de R$ 100.\nValor final: R$ {valor_com_desconto}')
                print(f'Maior produto: {produto_correspodente} R$ {produto_mais_caro}')
                break
        
            else:
                os.system('clear')
                print('Vamos encerrar o programa e exibir os resultados.')
                print(f'O total acumulado foi de: R$ {total_acumulado}.')
                print(f'Maior produto: {produto_correspodente} R$ {produto_mais_caro}')
                break