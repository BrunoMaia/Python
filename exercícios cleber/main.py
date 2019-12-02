
import math
import tkinter
## tela de boas vindas e abertura do programa
def Entrada():
	while True:
		entrada_usr = str(input("Digite o programa a ser executado: "))
		if entrada_usr == "16":
			print("Programa selecionado: 16")
		if entrada_usr == "17":
			print("Programa selecionado: 17")
			co = input("Qual o tamanho do cateto oposto? ")
			ca = input("Qual o tamanho do cateto adjacente? ")
			hp = math.sqrt((int(co)**2)+(int(ca)**2))
			print("A hipotenusa é igual a: {}".format(hp))
		if entrada_usr == "18":
			print("Programa selecionado: 18")	
		if entrada_usr == "19":
			print("Programa selecionado: 19")
		if entrada_usr == "20":
			print("Programa selecionado: 20")
		if entrada_usr == "21":
			print("Programa selecionado: 21")
		else:
			print("Digite o número do exercício, entre 16 e 21")
Entrada()
