import os
import time
os.system('cls')

# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados
# sobre o salário e número de filhos das famílias da cidade. A prefeitura deseja saber:  
# 
# a) total de famílias que responderam a pesquisa;
# b) média do salário da população;
# c) média do número de filhos;
# d) maior salário;
# e) menor salário.
# Crie um menu com duas opções.
# Código |   Descrição
#    1   |   Adicionar família
#    2   |   Sair e exibir resultados
# O final da leitura de dados se dará com 
# quando o usuário digitar o número código 2.

lista_de_familias = []
lista_de_filhos = [] 
lista_de_salarios = [] 
maior_salario = max(lista_de_salarios)
menor_salario = min(lista_de_salarios)



media_salario_da_populacao = sum(lista_de_salarios) / sum(lista_de_familias)
media_filhos = sum (lista_de_filhos) / sum(lista_de_familias)