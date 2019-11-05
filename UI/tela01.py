#Title: System ATMB Reformulado
#Organization: Private Project
#Screen1: Main Screen
#Description: Main Screen for the User Interface
#Author: Diego Vieira

from tkinter import *

class MainScreen:
    def __init__(self, master = None):
        #primeiro container
        self.moldura = Frame(master)
        self.moldura.grid(row = 0, column = 0, rowspan = 2, columnspan = 2, sticky = N)

        #elementos do titulo
        self.titulo = Label(self.moldura)
        self.titulo["font"] = ('MS', '30')
        self.titulo["text"] = "SYSTEM ATMB"
        self.titulo.pack(side = TOP, fill = X)

        #elementos do subtitulo
        self.subtitulo = Label(self.moldura)
        self.subtitulo["font"] = ('MS','12','underline')
        self.subtitulo["text"] = "Software Educativo de Musicografia Braile"
        self.subtitulo.pack(side = TOP, fill = X)

        #elementos de botao
        self.fonte_padrao = ('Arial','10','underline')

        self.botao_historico = Button(master)
        self.botao_historico["text"] = "Histórico"
        self.botao_historico["font"] = self.fonte_padrao
        self.botao_historico.grid(row = 2, column = 0, sticky = NW)

        self.cela_braile = Button(master)
        self.cela_braile["text"] = "Cela Braille"
        self.cela_braile["font"] = self.fonte_padrao
        self.cela_braile.grid(row = 2, column = 1, sticky = NW)

        self.teoria_musical = Button(master)
        self.teoria_musical["text"] = "Teoria Musical"
        self.teoria_musical["font"] = self.fonte_padrao
        self.teoria_musical.grid(row = 3, column = 0, sticky = NW)

        self.musicografia = Button(master)
        self.musicografia["text"] = "Musicografia Braille"
        self.musicografia["font"] = self.fonte_padrao
        self.musicografia.grid(row = 3, column = 1, sticky = NW)

        self.editor = Button(master)
        self.editor["text"] = "Software Musibraille"
        self.editor["font"] = self.fonte_padrao
        self.editor.grid(row = 4, column = 0, sticky = NW)

        self.exerc = Button(master)
        self.exerc["text"] = "Exercícios"
        self.exerc["font"] = self.fonte_padrao
        self.exerc.grid(row = 4, column = 1, sticky = NW)

root = Tk()
root.title("System ATMB")
MainScreen(root)
root.mainloop()