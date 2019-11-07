#Title: System ATMB Reformulado
#Organization: Private Project
#Screen2: Cela Braille
#Description: Third Screen on the App UX Flow
#Author: Diego Vieira

from tkinter import *

class ScreenCelaBraille:
    def __init__(self, master = None):
        self.moldura = Frame(master)
        self.moldura.pack()

        self.fonte_padrao = ('Arial','10','underline')

        self.titulo = Label(self.moldura)
        self.titulo["text"] = "Cela Braille"
        self.titulo["font"] = ('MS','30','underline')
        self.titulo.pack(side = TOP, fill = X)

        self.botao_um = Button(self.moldura)
        self.botao_um["text"] = "Estrutura da Cela Braille"
        self.botao_um["font"] = self.fonte_padrao
        self.botao_um.pack(side = TOP, fill = X)

        self.botao_dois = Button(self.moldura)
        self.botao_dois["text"] = "Alfabeto Braille"
        self.botao_dois["font"] = self.fonte_padrao
        self.botao_dois.pack(side = TOP, fill = X)

        self.botao_tres = Button(self.moldura)
        self.botao_tres["text"] = "Números"
        self.botao_tres["font"] = self.fonte_padrao
        self.botao_tres.pack(side = TOP, fill = X)

        self.botao_quatro = Button(self.moldura)
        self.botao_quatro["text"] = "Sinais Gráficos"
        self.botao_quatro["font"] = self.fonte_padrao
        self.botao_quatro.pack(side = TOP, fill = X)

        self.botao_cinco = Button(self.moldura)
        self.botao_cinco["text"] = "Exercícios"
        self.botao_cinco["font"] = self.fonte_padrao
        self.botao_cinco.pack(side = TOP, fill = X)

        self.opcoes = Frame(master)
        self.opcoes.pack()

        self.duvida = Button(self.opcoes)
        self.duvida["text"] = "?"
        self.duvida["font"] = self.fonte_padrao
        self.duvida.pack(side = LEFT)

        self.sair = Button(self.opcoes)
        self.sair["text"] = "X"
        self.sair["font"] = self.fonte_padrao
        self.sair.pack(side = LEFT)

root = Tk()
root.title("Cela Braille")
ScreenCelaBraille(root)
root.mainloop()