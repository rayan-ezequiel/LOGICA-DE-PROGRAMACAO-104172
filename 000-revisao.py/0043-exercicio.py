import os
os.system('cls')

# Faça um programa que leia e valide as seguintes informações:

    # Nome: maior que 3 caracteres;
    # Idade: entre 0 e 150;
    # Salário: maior que zero;
    # Sexo: 'f' ou 'm';
    # Estado Civil: 's', 'c', 'v', 'd';
    
while True:
    
    nome = input('Nome: ').lower()
    idade = int(input('Idade: ').lower())
    salario = int(input('salário: ').lower())
    sexo = input('Sexo: ').lower()
    estado_civil = input('Estado Civil: ').lower()
    
    if len(nome) > 3:
        print('nome validado com sucesso')
        
    if 0 >= idade <= 150:
        print('idade validada com sucesso')
            
    if salario > 0:
        print('salario validado com sucesso.')
                
    if sexo == 'm' or 'f':
        print('sexo validado com sucesso.')
                    
    if estado_civil == 's' and 'c' and 'v' and 'd':
        print('estado civil validado com sucesso.')
        break

    else: print('tente novamente...')

