import sqlite3 as conector
# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_banco.db")
conexao.execute("PRAGMA foreign_keys = on") # PRAGMA é utlizada para checagem de chave strangeira
cursor = conexao.cursor()

# cursor.close()
# conexao.close()