import defs_atualizar
import sqlite3

def incluir_disciplina(choose, disciplinas):
    conexao = sqlite3.connect('sistema_alunos/main.db')
    cursor = conexao.cursor()
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
                cursor.execute('INSERT INTO disciplinas (nome, area) VALUES (?, ?)', dados)
                conexao.commit()
                print('\n')
                print(f"Disciplina {disciplina_nome} adicionada.")
                break

            case '2' | 'exatas':
                dados = (disciplina_nome, 'exatas')
                cursor.execute('INSERT INTO disciplinas (nome, area) VALUES (?, ?)', dados)
                conexao.commit()
                print('\n')
                print(f"Disciplina {disciplina_nome} adicionada.")
                break

            # case '3' | 'ambas':
            #     dados = (disciplina_nome, 'ambas')
            #     cursor.execute('INSERT INTO disciplinas (nome, area) VALUES (?, ?)', dados)
            #     conexao.commit()
            #     print('\n')
            #     print(f"Disciplina {disciplina_nome} adicionada.")
            #     break

            case _:
                print('Valor inserido para área é inválido.')
                continue

    conexao.close()


def listar_disciplina(choose, disciplinas):
    conexao = sqlite3.connect('sistema_alunos/main.db')
    cursor = conexao.cursor()

    print(f"Opção escolhida foi: {choose.capitalize()}")

    cursor.execute('SELECT * FROM DISCIPLINAS')
    disciplinas = cursor.fetchall()
    print (disciplinas)

    print("Lista de disciplinas: ")
    for row in disciplinas:
        print(f'--Disciplina: {row[1]} | ID: {row[0]} | Área: {row[2]}')


def atualizar_disciplina(choose, disciplinas):
    conexao = sqlite3.connect('sistema_alunos/main.db')
    cursor = conexao.cursor()

    print(f"Opção escolhida foi: {choose.capitalize()}")
    atualizar = input('Qual o ID da disciplina que deseja atualizar?: ')
    cursor.execute('SELECT count(1) AS c FROM disciplinas WHERE id = ?', (atualizar, ))
    verifier = cursor.fetchone()

    if verifier[0] > 0:
        print('\n')
        # indice = defs_atualizar.pegarid_disciplinas (disciplinas, atualizar)
        print('E qual dado deseja atualizar?')
        print('1. Nome')
        print('2. Área')
        qual = str(input('E qual dado deseja atualizar?: '))


        match qual:

            case '1' | 'nome':
                novo_nome = input('Qual será o novo nome da disciplina?')
                cursor.execute('UPDATE disciplinas SET nome = ? WHERE id = ?', (novo_nome, atualizar ))
                conexao.commit()

            case '2' | 'area':
                nova_area = input('Qual será a nova área da disciplina?')
                cursor.execute('UPDATE disciplinas SET area = ? WHERE id = ?', (nova_area, atualizar ))
                conexao.commit()

            case _:
                print('Valor não encontrado')

    else: print('\n', 'Não existe uma disciplina com o ID inserido.')

    conexao.close()
                

def excluir_disciplinas(choose, disciplinas):
    conexao = sqlite3.connect('sistema_alunos/main.db')
    cursor = conexao.cursor()

    print(f"Opção escolhida foi: {choose.capitalize()}")

    excluir = input('Qual o ID da disciplina que deseja excluir?: ')

    cursor.execute('SELECT count(1) FROM disciplinas where id = ?', (excluir, ))
    verifier = cursor.fetchone()

    if verifier[0] > 0:
        cursor.execute('DELETE FROM disciplinas WHERE id = ?', (excluir))
        conexao.commit()


    else:
        print(f'Nenhuma disciplina com o ID {excluir} foi encontrado. ')
        

