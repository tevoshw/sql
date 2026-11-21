import sqlite3


conn = sqlite3.connect('teste.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS teste (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)""")

# Inserir dados na tabela
cursor.execute("INSERT INTO teste (nome, username, email, senha) VALUES (?, ?, ?, ?)", ("João", "joao123", "joao@gmail.com", "123456"))
cursor.execute("INSERT INTO teste (nome, username, email, senha) VALUES (?, ?, ?, ?)", ("Maria", "maria123", "maria@gmail.com", "123456"))
cursor.execute("INSERT INTO teste (nome, username, email, senha) VALUES (?, ?, ?, ?)", ("Pedro", "pedro123", "pedro@gmail.com", "123456"))

# Commit e fechar a conexão
conn.commit()
conn.close()