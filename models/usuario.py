from conexao import conexao, cursor

class User():
    def __init__(self,nome,cpf,altura,peso_inicial):
        self.cpf = cpf
        self.nome = nome
        self.altura = altura
        self.peso_inicial = peso_inicial
            
    def insert_user(nome,cpf,altura,peso_inicial):
        cursor = conexao.cursor()
        try:
            if len(cpf) == 0:
                print("O campo 'cpf' deve está preenchido")
                return None
            elif len(nome) == 0:
                print("O campo 'nome' deve está preenchido")
                return None
            elif len(altura) == 0:
                print("O campo 'altura' deve está preenchido")
                return None
            elif len(peso_inicial) == 0:
                print("O campo 'peso' deve está preenchido")
                return None

            if User.ListarPorCpf(cpf):
                print(f"Já existe um usuário com esse cpf = '{cpf}'")
                return None 
     
            user = User(nome,cpf,altura,peso_inicial)
            query = "INSERT INTO Usuario VALUES(:cpf,:nome,:altura,:peso_inicial)"
            cursor.execute(query,vars(user))
            conexao.commit()
            print("Usuário cadastrado com sucesso")
            cursor.close()
            conexao.close()
        except Exception as erro:
            print(erro)
    
    def update_user(nome,cpf,altura,peso_inicial):
        try:
            if not User.ListarPorCpf(cpf):
                 User.insert_user(nome,cpf,altura,peso_inicial)     
            user = User(nome,cpf,altura,peso_inicial)
            query = '''UPDATE Usuario SET nome= :nome, altura= :altura, peso_inicial=
            :peso_inicial WHERE cpf= :cpf;'''
            cursor.execute(query,vars(user))
            conexao.commit()
            print("Usuario atualizado com sucesso")
            # cursor.close()
            # conexao.close()
            return None
        except Exception as erro:
            print(erro)

    @classmethod
    def ListarPorCpf(cls, cpf):
        try:
            query = "SELECT * FROM Usuario WHERE cpf = :cpf"
            cursor.execute(query,{"cpf":cpf})
            resultado = cursor.fetchall()
            if resultado:
                return resultado
            return None
        except Exception as erro:
            print(erro)