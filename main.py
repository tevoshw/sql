import sqlite3


conn = sqlite3.connect('teste.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS teste (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL
)
""")

conn.commit()
conn.close()

print('Tabela criada com sucesso')