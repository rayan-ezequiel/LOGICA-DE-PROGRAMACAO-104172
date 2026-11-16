import os
os.system('cls' if os.name == 'nt' else 'clear')

def calcular_notas(nota1, nota2):
    resultado = (nota1 + nota2) / 2
    return resultado

print('= SOLICITANDO NOTAS =')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input ('Digte a segunda nota: '))

#
#
media = calcular_notas(nota1, nota2)


print('\n= EXIBINDO NOTAS =')
print(f'Média: {media}')
if media >= 7:
    print('APROVADO')
else: print('REPROVADO')