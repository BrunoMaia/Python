#------------------- importando -----------------
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
import tkinter as tk

# ------------------------------------------ Definindo funções -------------------------------------------
def get_amount(call):
    while True:
        amount = input("Qual o valor do(a) {}? R$ ".format(str(call)))
        try:
            val = float(amount)
            if val > 0:
                break
            else:
                print("O valor tem que ser maior de zero")
        except ValueError:
            print("O valor tem que ser um número")
    val = round(val,2)
    return val

#definindo a função de obtenção de valor natural, menos o zero
def get_value(call):
    while True:
        value = input("Qual a quantidade de {}?".format(str(call)))
        try:
            val = int(value)
            if val > 0:
                break
            else:
                print("A quantidade tem que ser maior que zero")
        except ValueError:
            print("A quantidade tem que ser um número")
    return val

#definindo função de confirmação
def confirma():
    yes = {'yes','y','ye','sim','s'}
    no = {'no','n','nao','não'}
    choice = input().lower()
    if choice in yes:
      print("Confirmado!")
      return True
    if choice in no:
      print("Não confirmado!")
      return False
    else:
      print("Entrada NÃO salva, tente novamente!")
      print("Confirme com 'sim' ou 'nao'")
      return False
        
# ------------------------------------------ Definindo classes -------------------------------------------
class Gasto:
  def __init__(self, data, tipo, valor, descricao):
    self.data = data
    self.tipo = tipo
    self.valor = round(float(valor),2)
    self.desc = str(descricao)

  def __str__(self):
    return 'lançamento do tipo {}, na data {}, no valor de R$ {} e descrito por <{}>'.format(str(self.tipo),str(self.data),str(self.valor),str(self.desc))

  def __add__(self, outro_gasto):
    valor_gasto_1 = self.valor
    valor_gasto_2 = outro_gasto.valor
    tipo_gasto_1 = str(self.tipo)
    tipo_gasto_2 = str(outro_gasto.tipo)
    if tipo_gasto_1 != tipo_gasto_2:
      pass
    if tipo_gasto_1 == tipo_gasto_2:
      soma_gasto = round(float(valor_gasto_1) +float(valor_gasto_2),2)
      return soma_gasto 

  def GetValorGasto(self):
    return self.valor
  
  def CriarNomeDado(self):
    chave_data = str(self.data)
    chave_mes = chave_data[2:4]
    chave_ano = chave_data[4:6]
    chave_valor = int(round(float(self.valor),0))
    nome_dado = str((chave_mes)+(chave_ano)+'_'+str(chave_valor))
    return nome_dado

  def SalvarDado(self):
    chave_data = str(self.data)
    chave_valor = int(round(float(self.valor),0))
    chave_mes = chave_data[2:4]
    chave_ano = chave_data[4:6]
    nome_array = str((chave_mes)+(chave_ano)+'.dat')
    array = open(nome_array, 'a')
    array.write('{},{},{},{},{}\n'.format(str(self.CriarNomeDado()),str(chave_data),str(self.tipo),str(self.valor),str(self.desc)))
    array.close()

  def AbrirDado(self):
    chave_data = str(self.data)
    chave_valor = int(round(float(self.valor),0))
    chave_mes = chave_data[2:4]
    chave_ano = chave_data[4:6]
    nome_array = str((chave_mes)+(chave_ano)+'.dat')
    array = open(nome_array, 'r')
    linha = array.readline().rstrip('\n')
    dado = []
    while linha:
      dado.append(linha.split(','))
      linha = array.readline()
    array.close()
    return dado
    
class Salario:
  def __init__(self, valor, data):
    self.valor = round(float(valor),2)
    self.data = data
    sal_nome = 'salário'

  def __str__(self):
    return 'Rendimento de R$ {} do dia {}'.format(str(self.valor),str(self.data))

  def GetDisperso(self):
    fatia_disperso = int(self.valor)*0.3
    return round(float(fatia_disperso),2)

  def GetRecorrente(self):
    fatia_recorrente = int(self.valor)*0.3
    return round(float(fatia_recorrente),2)

  def GetInvestimento(self):
    fatia_investimento = int(self.valor)*0.3
    return round(float(fatia_investimento),2)

  def GetOutrem(self):
    fatia_outrem = float(self.valor)*0.1
    return round(float(fatia_outrem),2)

  def SalvarDadoSal(self):
    chave_data = str(self.data)
    chave_valor = int(round(float(self.valor),0))
    chave_mes = chave_data[2:4]
    chave_ano = chave_data[4:6]
    nome_array = str((chave_mes)+(chave_ano)+'.dat')
    array = open(nome_array, 'a')
    array.write('{},{},{},{},{}\n'.format(str(sal_nome),str(chave_data),str(sal_nome),str(self.valor),str(self.desc)))
    array.close()

  def AbrirDadoSal(self):
    chave_data = str(self.data)
    chave_valor = int(round(float(self.valor),0))
    chave_mes = chave_data[2:4]
    chave_ano = chave_data[4:6]
    nome_array = str((chave_mes)+(chave_ano)+'.dat')
    array = open(nome_array, 'r')
    linha = array.readline().rstrip('\n')
    dado = []
    while linha:
      dado.append(linha.split(','))
      linha = array.readline()
    array.close()
    return dado

# ------------------------------------------ Início do código -------------------------------------------

class GUI(tk.Tk): #criado seguindo pythonprogramming.net/object-oriented-programming-crash-course-tkinter/
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)
    container = tk.Frame(self)
    container.pack(side="top", fill="both", expand = True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    self.frames = {}
    frame = JanelaInicial(container, self)
    self.frames[JanelaInicial] = frame
    frame.grid(row=0, column=0, sticky="nsew")
    self.show_frame(JanelaInicial)

  def show_frame(self, cont):
    frame = self.frames[cont]
    frame.tkraise()

class JanelaInicial(tk.Frame):
  def __init__(self, parent, controller):
    janela = tk.Toplevel.__init__(self,parent)
    janela.pack(bg='#ffffff')

    


app = GUI()
app.mainloop

###### Saída de testes 
rendimento = Salario(1544.888,111019)
disperso = rendimento.GetDisperso()
recorrente = rendimento.GetRecorrente()
investimento = rendimento.GetInvestimento()
outrem = rendimento.GetOutrem()
print('rendimento '+str(rendimento))
print('disperso '+str(disperso))
print('recorrente '+str(recorrente))
print('investimento '+str(investimento))
print('outrem '+str(outrem))
gasto_teste = Gasto(120119,'recorrente',544.6666,'compras no cartão parcelado 18x')
# gasto_teste.SalvarDado()
print(gasto_teste.AbrirDado())

# sal = get_amount("salário")
# print("Salvo: R$ {}".format(str(sal)))
# while True:
#   tipo_gasto = input("Qual o tipo de lançamento? ")
#   for i in tipo_gasto: 
#     if tipo_gasto.lower()=='r':
#       print("Selecionado: recorrente")
#       parcelas_tot = get_value("parcelas totais")
#       parcelas_fal = get_value("parcelas restantes")
#       if parcelas_fal>parcelas_tot:
#         print("Quantidade de parcelas totais menor que as restantes")
#         break
#       valor_parcela = get_amount("valor da parcela")
#       print("Confirma o gasto recorrente: de R${} em {} parcelas, faltando {} parcelas?".format(str(valor_parcela),str(parcelas_tot),+str(parcelas_fal))) 
#       #pensar em como retornar em caso de não confirmação

#     if tipo_gasto.lower()=='d':
#       print("Selecionado: disperso")
#       valor_gasto_d = get_amount("gasto disperso")
#       print("Confirma o gasto disperso de: R$ {}".format(str(valor_gasto_d)))  #mesmo do anterior  

#   if tipo_gasto.lower()=='i':
#     print("Selecionado: investimento")
#     valor_i = get_amount("investimento")
#     tipo_i = input("Qual o tipo de investimento? ")
#     print("Confirma o(a) {} de: R${}?".format(str(tipo_i),str(valor_i))) 
#     if confirma():
#       print("Salvo!")

#   if tipo_gasto.lower()=='o':
#     print("Selecionado: outrem")
#     valor_o = get_amount("gasto outrem")
#     print("Confirma o gasto Outrem de: R$ {}?".format(str(valor_o))) #mesmo
#   if tipo_gasto.lower()=='q':
#     break
#   elif tipo_gasto.isalpha():
#     print("\n" * 1)
#     print("Coloque <R> para recorrente, <I> para investimento, <O> para outrem, <D> para disperso e  <Q> para sair" )
#     print("\n" * 1)
# #----------------------- Calculos -------------------------
# print(" Fazendo calculos ".center(50, '-'))
# fatia_recorrente = int(sal)*0.3
# fatia_disperso = int(sal)*0.3
# fatia_investimento = int(sal)*0.3
# fatia_outrem = int(sal)*0.1
# print('A fatia do gasto recorrente é:')
# print(fatia_recorrente)
# print('A fatia do gasto disperso é:')
# print(fatia_disperso)
# print('A fatia de investimento é:')
# print(fatia_investimento)
# print('A fatia do gasto outrem é:')
# print(fatia_outrem)
# janela = Tk()
# janela.title("App de gestão financeira V0.1 -- By: Nott")
# janela.geometry('600x400')
# janela.configure(background='white')
# #janela.resizable(0,0)

# #- configurando janela ##########################################################

#------------------- entrada de dados -----------------
#definindo a função de obtenção de dinheiro

# self.label_dispersos = Label(master, text="Gastos dispersos",font=("arial",15), bg='#ffffff')
#     self.label_dispersos.place(y=20, x=20, rely=0.15)
#     self.titulo_janela = Label(master)
#     self.titulo_janela = Label(master, text='Finanças',font=("arial",30),bg='#827717',fg='#ffffff')
#     self.titulo_janela.place(relwidth=1,y=0,relheight=0.15)

#     self.dispersos_id = Label(master, text="Gastos dispersos",font=("arial",15), bg='#ffffff')
#     self.dispersos_id.place(y=20, x=20, rely=0.15)
#     self.dispersos_bar = Label(master)
#     self.dispersos_id = Label(master, text="$$$$$$$$$$",font=("arial",15), bg='#ffffff',fg='#65553b')
#     self.dispersos_id.place(y=20, x=200, rely=0.15,relwidth=0.3, width=5)
#     self.dispersos_gt = Label(master, text="R$1600,50",font=("arial",15), bg='#ffffff', fg='#626141')
#     self.dispersos_gt.place(y=20, x=380, rely=0.15,relwidth=0.3)

#     self.recorrentes_id = Label(master, text="Gastos recorrentes",font=("arial",15), bg='#ffffff')
#     self.recorrentes_id.place(y=60, x=20, rely=0.15)
#     self.recorrentes_bar = Label(master)
#     self.recorrentes_id = Label(master, text="$$$$$$$$$$$$$$$$$$$$",font=("arial",15), bg='#ffffff',fg='#65553b')
#     self.recorrentes_id.place(y=60, x=200, rely=0.15,relwidth=0.5, width=5)

#     self.investimento_id = Label(master, text="Investimentos",font=("arial",15), bg='#ffffff')
#     self.investimento_id.place(y=100, x=20, rely=0.15)
#     self.investimento_bar = Label(master)
#     self.investimento_id = Label(master, text="$$$$$$$$$$$$$$$$$$$$",font=("arial",15), bg='#ffffff',fg='#65553b')
#     self.investimento_id.place(y=100, x=200, rely=0.15,relwidth=0.5, width=5)

#     self.outrem_id = Label(master, text="Gastos outrem",font=("arial",15), bg='#ffffff')
#     self.outrem_id.place(y=140, x=20, rely=0.15)
#     self.outrem_bar = Label(master)
#     self.outrem_id = Label(master, text="$$$$$$$$$$$$$$$$$$$$",font=("arial",15), bg='#ffffff',fg='#65553b')
#     self.outrem_id.place(y=140, x=200, rely=0.15,relwidth=0.5, width=5)

#     self.botao_sair = Button(master, text='Sair')
#     self.botao_sair.place(anchor=S,x=200,y=300, rely=0.1, width=50)
#     self.disperso_id.pack(side=top)

