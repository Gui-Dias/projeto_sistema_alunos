import sqlite3
#oijoijio
def rundb():
    conexao = sqlite3.connect('sistema_alunos/main.db')

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
            FOREIGN KEY (estudante_id) REFERENCES ESTUDANTES(id)
            );

    ''')

    cursor.execute('''
        CREATE TABLE associa_professor_disciplina(
            id_disciplina INTEGER NOT NULL,
            id_professor INTEGER NOT NULL,
            PRIMARY KEY(id_disciplina, id_professor),
            FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id),
            FOREIGN KEY (id_professor) REFERENCES professores(id)'
        )
    ''')

    conexao.commit()
    conexao.close()
