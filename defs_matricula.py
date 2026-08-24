import random
import sqlite3

def gerador_matricula():
    matricula_gerador = random.randint(4001, 5999)

    conexao = sqlite3.connect('sistema_alunos/main.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT matricula FROM matriculas')

    existe = {linha[0] for linha in cursor.fetchall()}

    while matricula_gerador in existe:
        matricula_gerador = random.randint(4001, 5999)

    print(f"Matrícula única gerada com sucesso: {matricula_gerador}")

    conexao.close()
    return matricula_gerador