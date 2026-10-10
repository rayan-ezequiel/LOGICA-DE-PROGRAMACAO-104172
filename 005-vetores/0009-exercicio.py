import os
os.system('cls')

pedidos_totais = []

while True:
    
    print('Cardápio Restaurante')
    #esta bagunçado pois é o jeito que funciona para a visualização no terminal
    print('\n Código   |     Prato               |       Valor ')
    print('\n 1	  | Picanha	            | R$ 25,00 ')
    print('\n 2	  | Lasanha	            | R$ 20,00 ')
    print('\n 3	  | Strogonoff	            | R$ 18,00 ')
    print('\n 4	  | Bife Acebolado	    | R$ 15,00 ')
    print('\n 5	  | Pão com ovo	            | R$ 5,00 \n')
    
    pedido = int(input(f'Qual prato o senhor(a) deseja (Digite o código) ? \n'))
    pedidos_totais.append(pedido)

    continuar = int(input(('\nDeseja fazer mais algum pedido ? \nDigite 1 para sim e 2 para não: ')))
    if continuar == 1:
        continue
    else:
        print('\nConta final.')
        
        picanha_qtd = pedidos_totais.count(1)
        picanha_total = picanha_qtd * 25

        lasanha_qtd = pedidos_totais.count(2) 
        lasanha_total = lasanha_qtd * 20           

        strogonoff_qtd = pedidos_totais.count(3) 
        strogonoff_total = strogonoff_qtd * 18

        bife_acebolado_qtd = pedidos_totais.count(4)
        bife_acebolado_total = bife_acebolado_qtd * 15

        pao_com_ovo_qtd = pedidos_totais.count(5)
        pao_com_ovo_total = pao_com_ovo_qtd * 5

        if picanha_qtd > 0:
            print(f'\n{picanha_qtd}x  Picanha R$ 25 \nTotal: R$ {picanha_total}\n')
        if lasanha_qtd > 0:
            print(f'{lasanha_qtd}x Lasanha R$ 20 \nTotal: R$ {lasanha_total}\n')
        if strogonoff_qtd > 0:
            print(f'{strogonoff_qtd}x Strogonoff R$ 18 \nTotal: R$ {strogonoff_total}\n')
        if bife_acebolado_qtd > 0:
            print(f'{bife_acebolado_qtd}x Bife Acebolado R$ 15 \nTotal:R$ {bife_acebolado_total}\n')
        if pao_com_ovo_qtd > 0:
            print(f'{pao_com_ovo_qtd}x Pão com ovo R$ 5 \nTotal: R$ {pao_com_ovo_total}\n')
















    break


