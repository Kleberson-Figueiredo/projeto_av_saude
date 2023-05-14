import sqlite3 as conector

try:
    # Abertura de conexão e aquisição de cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    # Execução de um comando: SELECT... CREATE ...
    comando = '''CREATE TABLE usuario (
                    cpf TEXT NOT NULL,
                    nome TEXT NOT NULL,
                    altura FLOAT NOT NULL,
                    peso_inicial FLOAT NOT NULL,
                    PRIMARY KEY (cpf)
                    );'''

    cursor.execute(comando)
    
    comando1 = '''CREATE TABLE peso_semanal (
                    cpf TEXT NOT NULL,
                    data TIMESTAMP NOT NULL,
                    peso FLOAT NOT NULL,
                    PRIMARY KEY (data),
                    FOREIGN KEY(cpf) REFERENCES usuario(cpf)
                    );'''

    cursor.execute(comando1)



    # Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()