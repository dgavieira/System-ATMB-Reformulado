#Title: System ATMB Reformulado
#Organization: Private Project
#Screen2: Histórico da Musicografia Braile
#Description: Second Screen on the App UX Flow
#Author: Diego Vieira

from tkinter import *

class ScreenHistorico:
    def __init__(self, master = None):
        self.primeiroContainer = Frame(master)
        self.primeiroContainer.grid(row = 0, column = 0, rowspan = 5, columnspan = 5, sticky = NW)

        self.titulo = Label(self.primeiroContainer)
        self.titulo["font"] = ('MS', '30')
        self.titulo["text"] = "Histórico da Musicografia Braille"
        self.titulo.pack(side=TOP, fill=X)

        self.text = Text(self.primeiroContainer)
        self.scroll = Scrollbar(self.primeiroContainer)
        self.scroll["command"] = self.text.yview
        self.text.configure(yscrollcommand = self.scroll.set)
        self.text["height"] = 26
        self.text["width"] = 70
        self.text["font"] = ('MS','12')
        self.text.pack(side=LEFT)
        self.scroll.pack(side=RIGHT, fill=Y)

        self.fonte_padrao = ('Arial', '10')

        self.botao_um = Button(master)
        self.botao_um["text"] = "Ouvir"
        self.botao_um["font"] = self.fonte_padrao
        self.botao_um.grid(row = 1, column = 6, sticky = NW)

        self.botao_dois = Button(master)
        self.botao_dois["text"] = "Avançar"
        self.botao_dois["font"] = self.fonte_padrao
        self.botao_dois.grid(row = 2, column = 6, sticky = NW)

        self.botao_tres = Button(master)
        self.botao_tres["text"] = "Voltar"
        self.botao_tres["font"] = self.fonte_padrao
        self.botao_tres.grid(row = 3, column = 6, sticky = NW)

        self.botao_quatro = Button(master)
        self.botao_quatro["text"] = "Ouvir Texto Atual"
        self.botao_quatro["font"] = self.fonte_padrao
        self.botao_quatro.grid(row = 4, column = 6, sticky = NW)

        self.botao_cinco = Button(master)
        self.botao_cinco["text"] = "?"
        self.botao_cinco["font"] = self.fonte_padrao
        self.botao_cinco.grid(row = 5, column = 6, sticky = NW)

        self.botao_seis = Button(master)
        self.botao_seis["text"] = "Exercícios"
        self.botao_seis["font"] = self.fonte_padrao
        self.botao_seis.grid(row = 6, column = 6, sticky = NW)
root = Tk()
root.title("Histórico da Musicografia Braille")
ScreenHistorico(root)
root.mainloop()