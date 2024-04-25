#Import modules/libs
import sqlite3

# Connect to a .db file
conn = sqlite3.connect('aula.db')
c = conn.cursor()

# Function to print on screen the received data
def print_data(data):
    for row in data:
        print(row)

# Function that executes multiple queries to the database
def read_from_db():
    # Retrieve all students and their information
    print("Todos os alunos:")
    c.execute("SELECT * FROM Alunos")
    print_data(c.fetchall())

    # Retrieve all ages from all students
    print("\nTodas as idades:")
    c.execute("SELECT Idade FROM Alunos WHERE Idade > 18")
    print_data(c.fetchall())

    # Retrieve who has 'frozen' the course
    print("\nQuem trancou o curso?")
    c.execute("SELECT Nome FROM Alunos WHERE Situacao = 'Trancamento'")
    print_data(c.fetchall())

    # Retrieve who entered after 2012
    print("\nQuem entrou após 2012?")
    c.execute("SELECT Nome FROM Alunos WHERE Ingresso > 2012")
    print_data(c.fetchall())

    # Retrieve Patrick's age
    print("\nQual a idade de Patrick?")
    c.execute("SELECT Idade FROM Alunos WHERE Nome = 'Patrick'")
    print_data(c.fetchall())

    # Update the name of Pedro to Carlos
    print("\nMudando o nome de Pedro para Carlos...")
    c.execute("UPDATE Alunos SET Nome = 'Carlos' WHERE Nome = 'Pedro'")

    # Retrieve all students and their information (updated)
    print("Todos os alunos (atualizado):")
    c.execute("SELECT * FROM Alunos")
    print_data(c.fetchall())

# Execute all queries
read_from_db()

# Close the connection
c.close()
conn.close()
