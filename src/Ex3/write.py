import sqlite3

conn = sqlite3.connect('aula.db')
c = conn.cursor()

def create_table():
    c.execute(
        "CREATE TABLE IF NOT EXISTS Alunos(Nome TEXT, Matricula REAL, Idade INTEGER, Ingresso INTEGER, Situacao TEXT)"
    )

def data_entry():
    c.execute(
        """INSERT INTO Alunos(Nome, Matricula, Idade, Ingresso, Situacao) VALUES 
            ('Joao', 10114385, 28, 2022, 'Formado'),
            ('Pedro', 13100001, 25, 2020, 'Trancamento'),
            ('Maísa', 11280821, 26, 2023, 'Cursando'),
            ('Patrick', 14204123, 24, 2022, 'Desistiu');"""
    )

create_table()
data_entry()

conn.commit()
c.close()
conn.close()
