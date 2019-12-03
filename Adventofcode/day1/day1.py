from math import floor								# importar a função que faz o arredondamento para baixo

input_day1 = open('input_day1.txt', 'r') 			# abrir o arquivo com os inputs como apenas leitura			

def CalcularModulo(i):								# crio a função de cálculo de módulos, com base no site
	a = floor(int(i)/3) - 2							
	return a

combustivel = sum(map(CalcularModulo, input_day1))

print("O resultado é: {}".format(combustivel))
