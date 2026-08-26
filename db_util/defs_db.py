import sqlite3

caminho_db = 'db_util/main.db'

def rundb():
    conexao = sqlite3.connect('main.db')

    cursor = conexao.cursor()

    cursor.execute('PRAGMA foreign_keys = ON;')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(90),
            cpf INTERGER,
            id_sala INTEGER,
            FOREIGN KEY (id_sala) REFERENCES sala(id)
            );

    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS disciplinas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome varchar(90),
            area VARCHAR(10)
            );

    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(90),
            area VARCHAR(10),
            id_disciplina INTEGER,
            FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id)
            );

    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            materia varchar(90),
            periodo INTEGER
            );

    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matriculas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            matricula INTEGER,
            estudante_id INTEGER,
            FOREIGN KEY (estudante_id) REFERENCES estudantes(id)
            );

    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS associa_professor_disciplina(
            id_disciplina INTEGER NOT NULL,
            id_professor INTEGER NOT NULL,
            PRIMARY KEY(id_disciplina, id_professor),
            FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id),
            FOREIGN KEY (id_professor) REFERENCES professores(id)
            );
    ''')

    conexao.commit()
    conexao.close()


rundb()

def execute_clear(query):

    conexao = None

    try:
        conexao = sqlite3.connect(caminho_db)
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()

    finally:
        if conexao:
            conexao.close()



def excute_query(query, dados):

    try:
        conexao = sqlite3.connect(caminho_db)
        cursor = conexao.cursor()
        cursor.execute(query, dados)
        conexao.commit()

    finally:
        conexao.close()

def excute_query_return_id(query, dados):

    try:
        conexao = sqlite3.connect(caminho_db)
        cursor = conexao.cursor()
        cursor.execute(query, dados)
        id_gerado = cursor.lastrowid
        conexao.commit()
        conexao.close()
        return id_gerado

    finally:
        conexao.close()



def excute_query_fetchall(query, dados):
    conexao = None

    try:
        conexao = sqlite3.connect(caminho_db)
        cursor = conexao.cursor()
        cursor.execute(query, dados)
        fetchall = cursor.fetchall()
        conexao.commit()
        conexao.close()
        return fetchall

    finally:
        if conexao:
            conexao.close()




def excute_query_fetchone(query, dados):
    conexao = None

    try:
        conexao = sqlite3.connect(caminho_db)
        cursor = conexao.cursor()
        cursor.execute(query, dados)
        fetchone = cursor.fetchone()
        conexao.commit()
        conexao.close()
        return fetchone

    finally:
        if conexao:
            conexao.close()