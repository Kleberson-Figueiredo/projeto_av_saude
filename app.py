from models.usuario import User
from tkinter import *
from datetime import *

janela = Tk()
janela.title("Formulário")

textoUm = Label(janela, text="USUARIO:")
textoUm.grid(column=1, row=1, padx=5, pady=5)

jogador = Entry(janela, width=100)
jogador.grid(column=1, row=2, padx=10, pady=10)

textoDois = Label(janela, text="CPF:")
textoDois.grid(column=1, row=3, padx=5, pady=5)

hp = Entry(janela, width=100)
hp.grid(column=1, row=4, padx=10, pady=10)

textoTres = Label(janela, text="ALTURA:")
textoTres.grid(column=1, row=5, padx=5, pady=5)

mp = Entry(janela, width=100)
mp.grid(column=1, row=6, padx=5, pady=5)

textoQuatro = Label(janela, text="PESO:")
textoQuatro.grid(column=1, row=7, padx=10, pady=10)

classe = Entry(janela, width=100)
classe.grid(column=1, row=8, padx=5, pady=5)

botao = Button(janela, text="Cadastrar",
               command=lambda: User.update_user(jogador.get(), hp.get(), mp.get(), classe.get()))
botao.grid(column=2, row=2, padx=10, pady=10)

janela.mainloop()