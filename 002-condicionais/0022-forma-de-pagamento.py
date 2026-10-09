import os
os.system('cls')


print('Forma de pagamento')

valor_do_produto = int(input('Digite o valor do produto: '))
forma_de_pagamento = input('Deseja pagar a vista ou a prazo ? ').lower()
desconto = 0.10

match forma_de_pagamento:
    case 'a vista':
        print(f'Valor do produto: R$ {valor_do_produto}')
        print(f'Forma de pagamento: à vista')
        print(f'O valor do desconto: R${valor_do_produto * desconto}')
        print(f'Total a pagar: R$ {valor_do_produto - (desconto * 100)}')

    case 'a prazo':
        parcela = int(input('Quantas parcelas deseja pagar ? '))
        if parcela >= 1 or parcela <= 6 :
            print(f'Valor do produto: R$ {valor_do_produto}')
            print(f'Forma de pagamento: à prazo')
            print(f'Quantidade de parcelas: R${parcela}')
            print(f'Valor por parcela: R${valor_do_produto / parcela:.2f}')
            print(f'Total à prazo: R$ {valor_do_produto}')
    