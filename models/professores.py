import defs_atualizar
import sqlite3
import db_util.defs_db as db

def incluir_prof(choose):
    print(f"Opção escolhida foi: {choose.capitalize()}")

    nomeadd = input('Digite o nome do professor: ')
    nomeadd = nomeadd.lower()

    print('1. Humanas')
    print('2. Exatas')
    print('3. Ambas')
    areaadd = input('Qual área esse professor atua?: ')

    match areaadd:

        case '1' | 'humanas':
            query = 'INSERT INTO professores (nome, area) VALUES (?, ?)'
            dados = (nomeadd, 'humanas')
            id_gerado = db.excute_query_return_id(query, dados)
            print('\n')
            print(f"Professor {nomeadd} adicionado.")

        case '2' | 'exatas':
            query = 'INSERT INTO professores (nome, area) VALUES (?, ?)'
            dados = (nomeadd, 'exatas')
            id_gerado = db.excute_query_return_id(query, dados)
            print('\n')
            print(f"Professor {nomeadd} adicionado.")

        case '3' | 'ambas':
            query = 'INSERT INTO professores (nome, area) VALUES (?, ?)'
            dados = (nomeadd, 'ambas')
            id_gerado = db.excute_query_return_id(query, dados)
            print('\n')
            print(f"Professor {nomeadd} adicionado.")


    query = 'SELECT area FROM professores WHERE id = ?'
    area_prof = db.excute_query_fetchone(query, (id_gerado, ))



    disc = input('Deseja adicionar uma disciplina a esse professor? (y/n): ')

    while disc == 'y':

        print(f"Opção escolhida foi: {choose.capitalize()}")

        if area_prof[0] == 'ambas':
            query = 'SELECT * FROM DISCIPLINAS'
            disciplinas = db.excute_query_fetchall(query, '')

        else:
            query = 'SELECT * FROM disciplinas WHERE area = ?'
            disciplinas = db.excute_query_fetchall(query, area_prof)

        print("Lista de disciplinas: ")
        for row in disciplinas:
            print(f'--Disciplina: {row[1]} | ID: {row[0]} | Área: {row[2].capitalize()}')


        id_disc = input('Qual o id da disciplina que deseja adicionar ao professor?: ')

        query = 'SELECT count(1) from disciplinas d where id = ?'
        existe = db.excute_query_fetchone(query, id_disc)

        query = 'SELECT count(1) from associa_professor_disciplina where id_disciplina = ? AND id_professor = ?'
        dados = (id_disc, id_gerado)
        link_exists = db.excute_query_fetchone(query, dados)

        query = 'SELECT area FROM disciplinas WHERE id = ?'
        area_disc = db.excute_query_fetchone(query, (id_disc, ))

        if existe[0] > 0 and link_exists[0] < 1 and (area_disc[0] == area_prof[0] or area_prof[0] == 'ambas'):
            query = 'INSERT INTO associa_professor_disciplina (id_disciplina, id_professor) VALUES (?, ?)'
            dados = (id_disc, id_gerado)

            db.excute_query(query, dados)

        elif link_exists[0] > 0:
            print('\n''Esse professor já foi adicionado a essa matéria.')

        else: print('Matéria não encontrada.') 

        disc = input('Deseja adicionar uma disciplina a esse professor? (y/n): ')
            






def listar_prof(choose):
    print(f"Opção escolhida foi: {choose.capitalize()}")
    print("Lista de professores: ")

    query = 'SELECT p.id, p.nome, p.area FROM professores p'
    professores = db.excute_query_fetchall(query, '')

    for professor in professores:
        print(f'ID: {professor[0]}, Nome: {professor[1].capitalize()}, Área: {professor[2].capitalize()}')



def atualizar_prof(choose):
    print(f"Opção escolhida foi: {choose.capitalize()}")
    atualizar = input('Qual o ID do professor que deseja atualizar?: ')
    print('1. Nome')
    print('2. Área de atuação')
    qual = str(input('E qual dado deseja atualizar?: '))

    match qual:

        case '1':
            defs_atualizar.id_professores_edit(professores, indice)

        case '2':
            defs_atualizar.professor_edit(professores, indice)

        case '3':
            defs_atualizar.area_edit(professores, indice)

        case _:
            print('Valor não encontrado')
            

def excluir_prof(choose):
    print(f"Opção escolhida foi: {choose.capitalize()}")
    excluir = input('Qual o ID do professor que deseja excluir?: ')
    encontrou = False
    for professor in professores:
        if excluir == professor['id']:
            professores.remove(professor)
            encontrou = True
            break

    if not encontrou:
        print(f'Nenhum professor com o ID {excluir} foi encontrado.')
        

