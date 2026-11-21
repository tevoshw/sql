import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('teste.db')
cursor = conn.cursor()

# Selecionar todos os usuários
cursor.execute("SELECT * FROM teste")
users = cursor.fetchall()

for user in users:
    print(f"ID: {user[0]}, Nome: {user[1]}, Username: {user[2]}, Email: {user[3]}, Senha: {user[4]}")
    print("--------------------------------")
# Fechar a conexão
conn.close()
