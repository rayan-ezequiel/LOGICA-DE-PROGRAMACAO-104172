import os
os.system('cls')


print('Digite a população abaixo referente aos paises.')
pop_a = float(input('País A: '))
pop_b = float(input('País B: '))
quantidade_a = pop_a
quantidade_b = pop_b

taxa_a = float(input('Digite a taxa do país A: ')) / 100
taxa_b = float(input('Digite a taxa do país B: ')) / 100



#quantidade de anos que vai ultrapassar
anos_a = 0
anos_b = 0


while True:
    
    crescimento_anual_a = (pop_a * taxa_a)
    quantidade_a += crescimento_anual_a
    anos_a += 1

    crescimento_anual_b = (pop_b * taxa_b)
    quantidade_b += crescimento_anual_b

    if pop_a > pop_b:
        print(f'O país A será maior que país B em {anos_a}.')
    elif pop_b > pop_a:
        print(f'O país A será maior que país B em {anos_b}.')
    break
