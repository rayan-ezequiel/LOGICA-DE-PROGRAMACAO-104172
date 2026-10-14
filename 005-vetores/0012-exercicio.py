import os
os.system('cls')

nomes_livros = []
vez = 1
for i in range(5):
    nomes_livros.append(input(f'Digite o {vez}º nome do livro: '))
    vez += 1
print('Nome dos livros.')
print(F'{nomes_livros[0]}, {nomes_livros[1]}, {nomes_livros[2]}, {nomes_livros[3]}, {nomes_livros[4]}')