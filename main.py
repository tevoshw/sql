import sqlite3


conn = sqlite3.connect('teste.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS teste (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
    )

""")

# Inserir dados na tabela
nome_input = "João"
username_input = "joao123"
email_input = "joao@gmail.com"
senha_input = "123456"



cursor.execute("""

INSERT INTO teste (
    nome, 
    username, 
    email, 
    senha
)

VALUES (?, ?, ?, ?)
""", (nome_input, username_input, email_input, senha_input))


# Commit e fechar a conexão
conn.commit()
conn.close()