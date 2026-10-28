# 2. Filtro de Aprovados e Média da Turma VETOR ESFOR ESTATÍSTICA
# Peça ao usuário para digitar a nota final de 8 alunos e armazene todas em um vetor. 
# Calcule a média geral da
# turma, conte quantos alunos ficaram com nota igual ou superior a 7.0 e 
# exiba apenas a lista das notas dos
# alunos aprovado. 

import os
os.system('clear')

notas_da_turma = []
maior_que_sete = []

for i in range(8):
    nota = float(input('Digite sua nota final: '))
    notas_da_turma.append(nota)
    if nota >= 7:
        maior_que_sete.append(nota)
    media_geral_da_turma = sum(notas_da_turma) / len(notas_da_turma)
        
print(f'Média Geral da Turma: {media_geral_da_turma}.\nNotas aprovadas: {maior_que_sete}.')

