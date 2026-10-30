import os
os.system('cls')
# O QUE O PROGRAMA FAZ ? 
# Recebe o valor de dias que iriei gastar ida e volta do senai, depois ele calcula usando o valor da passagem
# meia do meu cartao de 2.95 reais, eventualmente tera dias que eu vou me abster de pagar a ida para o curso
# pois eu estaria indo do trabalho, e esse valor seria subtraido, pois ficaria na conta do emprego
meia_passagem = 2.95
passagem_inteira = 5.90

while True:
    dias = int(input('Quantos dias vou ao curso este mês: '))
    work_dias = int(input('Quantos desses dias, eu vou depois do trabalho: '))

    gasto_do_curso = dias * (meia_passagem * 2)
    pos_trabalho = work_dias * passagem_inteira

    if pos_trabalho > 0:
        total = gasto_do_curso - pos_trabalho
        print(f'\nGasto do mês curso: R$ {gasto_do_curso:.2f}\nO Trabalho vai paga: R$ {pos_trabalho:.2f}\nTotal: R$ {total:.2f}')
        break
    else:
        print(f'\nVocê gastará: R$ {gasto_do_curso:.2f}, este mês, sem gastos de trabalho.\n')
        break
