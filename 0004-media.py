import os 

#limpar terminal 

os.system('cls')

print('= SOLICITANDO DADOS =')

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
primeira_nota = float(input('Digite sua primeira nota: '))
segunda_nota = float(input('Digite sua segunda nota: '))

media = ((primeira_nota + segunda_nota)) /2 


print('\n= EXIBINDO DADOS =')
print('Nome: ', nome)
print('Idade: ', idade)
print('Sua primeira nota foi: ', primeira_nota)
print('Sua segunda nota foi:', segunda_nota)
print('a media é: ', media)

