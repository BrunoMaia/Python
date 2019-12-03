from math import floor								# importar a função que faz o arredondamento para baixo

input_day1 = open('input_day1.txt', 'r') 			# abrir o arquivo com os inputs como apenas leitura
valor = input_day1.readline() 						# definir que os valores são as leituras de cada linha de arquivo
dado = []											# criar uma lista vazia, que conterá os dados
while valor:										# loop, para executar enquanto houverem valores
	dado.append(valor.rstrip('\n'))					# adiciono a lista dado os valores, removendo à direita os símbolos de criação de linha '\n'
	valor = input_day1.readline()					# reeabro o valor, para continuar o loop (?)
input_day1.close()									# fecho o arquivo de dados

def CalcularModulo(i):								# crio a função de cálculo de módulos, com base no site
	a = floor(int(i)/3) - 2							
	return a

modulos = map(CalcularModulo, dado)
combustivel = sum(modulos)
print("O resultado é: {}".format(combustivel))