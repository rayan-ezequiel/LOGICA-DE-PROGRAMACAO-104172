import os
os.system('cls')

#menu
print('Código | Descrição')
print('  1    | Adicionar pessoa')
print('  2    | Exibir resultados')
print('  3    | Sair')

idade_list = []
sexo_list = []
salario_list = []
while True:
    escolha = int(input('Escolha: '))
    if escolha == 1:
        idade = int(input('Digite sua idade: '))
        idade_list.append(idade)
        print('M | Masculino')
        print('F | Feminino')
        sexo = input('Digite: ').lower()
        sexo_list.append(sexo)
        salario = int(input('Media salarial: '))
        salario_list.append(salario)
        continue
    elif escolha 2:
        
