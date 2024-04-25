# Import modules/libs
import sqlite3

# Create and connect to a .db file
conn = sqlite3.connect('aula.db')
c = conn.cursor()

# Function to create the 'Alunos' table, if not existent
def create_table():
    c.execute(
        "CREATE TABLE IF NOT EXISTS Alunos(Nome TEXT, Matricula REAL, Idade INTEGER, Ingresso INTEGER, Situacao TEXT)"
    )

# Function to populate the 'Alunos' table with some data
def data_entry():
    c.execute(
        """INSERT INTO Alunos(Nome, Matricula, Idade, Ingresso, Situacao) VALUES 
            ('Joao', 10114385, 28, 2022, 'Formado'),
            ('Pedro', 13100001, 25, 2020, 'Trancamento'),
            ('Maísa', 11280821, 26, 2023, 'Cursando'),
            ('Patrick', 14204123, 24, 2022, 'Desistiu');"""
    )

# Create table and populate it
create_table()
data_entry()

# Commit and close the connection
conn.commit()
c.close()
conn.close()
