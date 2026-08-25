import random
import sqlite3
import db_util.defs_db as defs_db

def gerador_matricula():
    matricula_gerador = random.randint(4001, 5999)

    query = 'SELECT matricula FROM matriculas'
    fetchall = defs_db.excute_query_fetchall(query, '')

    existe = {linha[0] for linha in fetchall}

    while matricula_gerador in existe:
        matricula_gerador = random.randint(4001, 5999)

    print(f"Matrícula única gerada com sucesso: {matricula_gerador}")

    return matricula_gerador