import sqlite3

conn = sqlite3.connect('aula.db')
c = conn.cursor()

def create_table():
    c.execute(
        "CREATE TABLE IF NOT EXISTS Alunos(Nome TEXT, Matricula REAL, Idade INTEGER, Ingresso INTEGER, Situacao TEXT)"
    )

def data_entry():
    c.execute(
        "INSERT INTO Alunos VALUES('Pedro', 2213482, 19, 2022, 'Cursando')"
    )

create_table()
data_entry()

conn.commit()
c.close()
conn.close()
