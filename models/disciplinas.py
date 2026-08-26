import defs_atualizar
import sqlite3
import db_util.defs_db as defs_db

def incluir_disciplina(choose):
    print(f"Opção escolhida foi: {choose.capitalize()}")

    while True:
        disciplina_nome = input('Digite o nome da disciplina: ')
        disciplina_nome = disciplina_nome.lower()

        print('1. Humanas')
        print('2. Exatas')
        area = input('Digite qual a área da disciplina?: ')
        area = area.lower()

        match area:

            case '1' | 'humanas':
                dados = (disciplina_nome, 'humanas')
                query = 'INSERT INTO disciplinas (nome, area) VALUES (?, ?)'
                defs_db.excute_query(query, dados)
                print('\n')
                print(f"Disciplina {disciplina_nome} adicionada.")
                break

            case '2' | 'exatas':
                dados = (disciplina_nome, 'exatas')
                query = 'INSERT INTO disciplinas (nome, area) VALUES (?, ?)'
                defs_db.excute_query(query, dados)
                print('\n')
                print(f"Disciplina {disciplina_nome} adicionada.")
                break


            case _:
                print('Valor inserido para área é inválido.')
                continue



def listar_disciplina(choose):

    print(f"Opção escolhida foi: {choose.capitalize()}")

    query = 'SELECT * FROM disciplinas'
    disciplinas = defs_db.excute_query_fetchall(query, '')
    
    print (disciplinas)

    print("Lista de disciplinas: ")
    for row in disciplinas:
        print(f'--Disciplina: {row[1]} | ID: {row[0]} | Área: {row[2].capitalize()}')



def atualizar_disciplina(choose):

    print(f"Opção escolhida foi: {choose.capitalize()}")
    atualizar = input('Qual o ID da disciplina que deseja atualizar?: ')
    query = 'SELECT count(1) AS c FROM disciplinas WHERE id = ?'
    verifier = defs_db.excute_query_fetchone(query, (atualizar, ))

    if verifier[0] > 0:
        print('\n')
        print('E qual dado deseja atualizar?')
        print('1. Nome')
        print('2. Área')
        qual = str(input('E qual dado deseja atualizar?: '))


        match qual:

            case '1' | 'nome':
                novo_nome = input('Qual será o novo nome da disciplina?')
                dados = (novo_nome, atualizar)
                query = 'UPDATE disciplinas SET nome = ? WHERE id = ?'
                defs_db.excute_query(query, dados)

            case '2' | 'area':
                print('1. Humanas')
                print('2. Exatas')
                nova_area = input('Digite qual a nova área da disciplina?: ')
                nova_area = nova_area.lower()

                while True:
                    match nova_area:

                        case '1' | 'humanas':
                            dados = (atualizar)
                            query = 'UPDATE disciplinas SET area = "humanas" WHERE id = ?'
                            defs_db.excute_query(query, dados)
                            break

                        case '2' | 'exatas':
                            dados = (atualizar)
                            query = 'UPDATE disciplinas SET area = "exatas" WHERE id = ?'
                            defs_db.excute_query(query, dados)
                            break


                        case _:
                            print('Valor inserido para área é inválido.')
                            continue

    else: print('\n', 'Não existe uma disciplina com o ID inserido.')
                

def excluir_disciplinas(choose):

    print(f"Opção escolhida foi: {choose.capitalize()}")

    excluir = input('Qual o ID da disciplina que deseja excluir?: ')

    query = 'SELECT count(1) FROM disciplinas WHERE id = ?'
    verifier = defs_db.excute_query_fetchone(query, (excluir, ))

    if verifier[0] > 0:
        query = 'DELETE FROM disciplinas WHERE id = ?'
        defs_db.excute_query(query, (excluir, ))

    else:
        print(f'Nenhuma disciplina com o ID {excluir} foi encontrado. ')
