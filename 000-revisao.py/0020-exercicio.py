import os
import time
os.system('cls' if os.name == 'nt' else 'clear') 

# Consulta de Estoque da Loja VETORES PARALELOSWHILE BUSCA
# Monte uma lista fixa com 5 produtos e outra com suas respectivas quantidades em estoque. Permita que o
# usuário consulte produtos repetidamente. Se a quantidade for menor que 5 unidades, exiba o alerta "Estoque
# Baixo!". O laço encerra ao digitar "sair"

nomes = ["Notebook", "Mouse", "Teclado", "Monitor", "Cadeira"]
quantidades = [15, 42, 28, 10, 5]

print("Produto    | Quantidade")
print("-----------------------")
print(f"1 - {nomes[0]}   | {quantidades[0]}")
print(f"2 - {nomes[1]}      | {quantidades[1]}")
print(f"3 - {nomes[2]}    | {quantidades[2]}")
print(f"4 - {nomes[3]}    | {quantidades[3]}")
print(f"5 - {nomes[4]}    | {quantidades[4]}")
print("0 - Sair")

while True:
    try:
        escolha = int(input('Escolha: '))
    except ValueError:
        print('Apenas números inteiros...')

    match escolha:
        
        
        case 1:
            print(f'Produto: {nomes[0]}.\nQuantidade: {quantidades[0]}.')
            
            if quantidades[0] == 0:
                print('Sem estoque...')
                time.sleep(2)
                continue
            elif quantidades[0] < 5:
                print('Estoque Baixo...')
                time.sleep(2)
                continue
            else:
                quantidades[0] -= 1
                continue
        case 2:

            print(f'Produto: {nomes[1]}.\nQuantidade: {quantidades[1]}.')
            
            if quantidades[1] == 0:
                print('Sem estoque...')
                time.sleep(2)
                continue
            elif quantidades[1] < 5:
                print('Estoque Baixo...')
                time.sleep(2)
                continue
            else:
                quantidades[1] -= 1
                continue
        case 3:
            print(f'Produto: {nomes[2]}.\nQuantidade: {quantidades[2]}.')
                        
            if quantidades[2] == 0:
                print('Sem estoque...')
                time.sleep(2)
                continue
            elif quantidades[2] < 5:
                print('Estoque Baixo...')
                time.sleep(2)
                continue
            else:
                quantidades[2] -= 1
                continue
        case 4:
            print(f'Produto: {nomes[3]}.\nQuantidade: {quantidades[3]}.')
                        
            if quantidades[3] == 0:
                print('Sem estoque...')
                time.sleep(2)
                continue
            elif quantidades[3] < 5:
                print('Estoque Baixo...')
                time.sleep(2)
                continue
            else:
                quantidades[3] -= 1
                continue
        case 5:
            print(f'Produto: {nomes[4]}.\nQuantidade: {quantidades[4]}.')
                        
            if quantidades[4] == 0:
                print('Sem estoque...')
                time.sleep(2)
                continue
            elif quantidades[4] < 5:
                print('Estoque Baixo...')
                time.sleep(2)
                continue
            else:
                quantidades[4] -= 1
                continue
        case 0:
            print('Saindo do programa...')
            time.sleep(2)
            break