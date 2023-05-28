import tkinter as tk
from models.usuario import User

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        
        self.frames = {}
        
        self.add_frame(HomePage)
        self.add_frame(Page1)
        self.add_frame(Page2)
        
        self.show_frame(HomePage)
        
    def add_frame(self, frame_class):
        frame = frame_class(self.container, self)
        self.frames[frame_class] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        
    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()
        
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="IMC Home")
        label.pack(pady=10, padx=10)
        
        button1 = tk.Button(self, text="Cadastrar informações", command=lambda: controller.show_frame(Page1))
        button1.pack(pady=(0, 0), padx=(150, 10), side="left")
        
        button2 = tk.Button(self, text="Visualizar progresso", command=lambda: controller.show_frame(Page2))
        button2.pack(pady=(0, 0), padx=(10, 150), side="right")
        
class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Usuário:")
        label.pack(pady=(10, 0), padx=0)

        usuario = tk.Entry(self, width=100,)
        usuario.pack(pady=10, padx=10)

        textoDois = tk.Label(self, text="CPF:")
        textoDois.pack(padx=5, pady=(10, 0))

        cpf = tk.Entry(self, width=100)
        cpf.pack( padx=10, pady=10)

        textoTres = tk.Label(self, text="Altura:")
        textoTres.pack(padx=5, pady=(10, 0))

        altura = tk.Entry(self, width=100)
        altura.pack( padx=5, pady=5)

        textoQuatro = tk.Label(self, text="Peso:")
        textoQuatro.pack( padx=10, pady=(10, 0))

        peso = tk.Entry(self, width=100)
        peso.pack(padx=5, pady=5)

        botao = tk.Button(self, text="Cadastrar",
                    command=lambda: User.insert_user(usuario.get(), cpf.get(), altura.get(), peso.get()))
        botao.pack(side="left", padx=(150, 10), pady=10)
        
        button = tk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage))
        button.pack(side="right", padx=(10, 150), pady=10)
        
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Aqui é a página onde vai ser o gráfico.")
        label.pack(pady=10, padx=10)
        
        button = tk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage))
        button.pack()

app = App()
app.mainloop()
