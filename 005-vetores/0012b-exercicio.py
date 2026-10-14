import os
os.system('cls')

nomes_livros = []
for i in range(5):
    nomes_livros.append(input(f'Digite o {i+1}º nome do livro: '))
    
print('Nome dos livros.')
for i, livro in enumerate(nomes_livros, start=1):
    print(f'{i}º: {livro}')