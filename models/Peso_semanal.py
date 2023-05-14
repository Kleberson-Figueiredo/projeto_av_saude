from conexao import conexao, cursor

class peso_semanal():
    def __init__(self,cpf,data,peso):
        self.cpf = cpf
        self.data = data
        self.peso = peso
            
    def insert(cpf,data,peso):
        try:            
            cursor = conexao.cursor()

            if peso_semanal.ListarUltimaData() == None:
                query = "INSERT INTO peso_semanal VALUES(:cpf,:data,:peso)"
                cursor.execute(query,{"cpf": cpf, "data": data, "peso": peso})
                conexao.commit()
                print("Peso inserido com sucesso")
                cursor.close()
                conexao.close()
                return None
                
            data_bd = peso_semanal.ListarUltimaData()[0][1]
            data_calc = str(data_bd).replace("-","")
            data_real = str(data).replace("-","")
            resultado = (int(data_calc)-int(data_real))+7
            print(resultado)
            
            if len(cpf) == 0:
                print("O campo 'cpf' deve está preenchido")
                return None
            # elif len(data) == 0:
            #     print("O campo 'nome' deve está preenchido")
            #     return None
            elif len(peso) == 0:
                print("O campo 'altura' deve está preenchido")
                return None

            if peso_semanal.ListarPorData(data):
                print(f"Já existe cadastro para essa data = '{data}'")
                return None
            
            if resultado > -1:
                print(f"Faça o proximo cadastro do peso em {resultado} dia's")
                return
            
            query = "INSERT INTO peso_semanal VALUES(:cpf,:data,:peso)"
            cursor.execute(query,{"cpf": cpf, "data": data, "peso": peso})
            conexao.commit()
            print("Peso inserido com sucesso")
            cursor.close()
            conexao.close()
        except Exception as erro:
            print(erro)
    
    def update(cpf,data,peso):
        try:
            if not peso_semanal.ListarPorData(data):
                print("Data não cadastrda")
                return None
                 
            peso_semanal(cpf,data,peso)
            query = '''UPDATE peso_semanal SET cpf= :cpf, peso=
            :peso WHERE data= :data;'''
            cursor.execute(query,{"cpf":cpf, "peso":peso, "data":data})
            conexao.commit()
            print("Dados atualizado com sucesso")
            cursor.close()
            conexao.close()
            return None
        except Exception as erro:
            print(erro)

    @classmethod
    def ListarPorData(cls, data):
        try:
            query = "SELECT * FROM peso_semanal WHERE data = :data"
            cursor.execute(query,{"data":data})
            resultado = cursor.fetchall()
            if resultado:
                return resultado
            return None
        except Exception as erro:
            print(erro)
    
    @classmethod
    def ListarUltimaData(cls):
        try:
            query = "SELECT *FROM peso_semanal WHERE data = (SELECT MAX( data ) FROM peso_semanal);"
            cursor.execute(query)
            resultado = cursor.fetchall()
            if resultado:
                return resultado
            return None
        except Exception as erro:
            print(erro)