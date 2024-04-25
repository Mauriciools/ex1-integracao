import sqlite3

conn = sqlite3.connect('aula.db')
c = conn.cursor()

def print_data(data):
    for row in data:
        print(row)

def read_from_db():
    print("Todos os alunos:")
    c.execute("SELECT * FROM Alunos")
    print_data(c.fetchall())

    print("\nTodas as idades:")
    c.execute("SELECT Idade FROM Alunos WHERE Idade > 18")
    print_data(c.fetchall())

    print("\nQuem trancou o curso?")
    c.execute("SELECT Nome FROM Alunos WHERE Situacao = 'Trancamento'")
    print_data(c.fetchall())

    print("\nQuem entrou após 2012?")
    c.execute("SELECT Nome FROM Alunos WHERE Ingresso > 2012")
    print_data(c.fetchall())

    print("\nQual a idade de Patrick?")
    c.execute("SELECT Idade FROM Alunos WHERE Nome = 'Patrick'")
    print_data(c.fetchall())

    print("\nMudando o nome de Pedro para Carlos...")
    c.execute("UPDATE Alunos SET Nome = 'Carlos' WHERE Nome = 'Pedro'")

    print("Todos os alunos (atualizado):")
    c.execute("SELECT * FROM Alunos")
    print_data(c.fetchall())

read_from_db()
c.close()
conn.close()
