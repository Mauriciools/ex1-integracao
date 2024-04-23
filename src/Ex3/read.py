import sqlite3

conn = sqlite3.connect('aula.db')
c = conn.cursor()

def read_from_db():
    c.execute('SELECT * FROM Alunos')
    data = c.fetchall()

    for row in data:
        print(row)

    c.execute('SELECT Idade FROM Alunos WHERE Idade > 18')
    data = c.fetchall()

    for row in data:
        print(row)

read_from_db()
c.close()
conn.close()
