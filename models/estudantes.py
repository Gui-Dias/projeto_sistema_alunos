import defs_atualizar
import models.matricula as matricula
import sqlite3
import db_util.defs_db as defs_db

def incluir_est(choose):
    print(f"Opção escolhida foi: {choose.capitalize()}")

    id_gerado = 0
    while True:

        nomeadd = str(input('Digite o nome do estudante: '))
        nomeadd = nomeadd.lower()



        try:
            cpfadd = int(input('Digite o CPF do estudante (apenas os números, 11 digitos): '))

            if len(str(cpfadd)) == 11:
                break

            else:
                print('Dados digitados inválidos', '\n')

        except ValueError:
            print('Formato do valor inserido está incorreto.')
            continue

    dados = (nomeadd, cpfadd)
    sql = '''
    INSERT INTO estudantes (nome, cpf) VALUES (?, ?);
    '''

    id_gerado = defs_db.excute_query_return_id(sql, dados)
    print(f"Estudante {nomeadd} de id {id_gerado} adicionado.")


    matricula_num = matricula.gerador_matricula()

    matricula_id = (matricula_num, id_gerado)

    sql = '''
    INSERT INTO matriculas (matricula, estudante_id) VALUES (?, ?);
    '''
    defs_db.excute_query(sql, matricula_id)





def listar_est(choose):
    
    print(f"Opção escolhida foi: {choose.capitalize()}")
    print("Lista de estudantes: ")
    # conexao = sqlite3.connect('db_util/main.db')
    # cursor = conexao.cursor()

    query = """
        SELECT e.id, e.nome, e.cpf, m.matricula 
        FROM estudantes e
        INNER JOIN matriculas m ON e.id = m.estudante_id
    """
    
    resultados = defs_db.excute_query_fetchall(query, '')

    for row in resultados:
        estudante_id = row[0]
        nome_estudante = row[1]
        nome_estudante = nome_estudante.capitalize()
        cpf_estudante = row[2]
        matricula_atual = row[3]
        
        print(f'ID: {estudante_id} | Nome: {nome_estudante} | CPF: {cpf_estudante} | Matricula: {matricula_atual}')






def atualizar_est(choose):
    print(f"Opção escolhida foi: {choose.capitalize()}")
    atualizar = int(input('Qual o ID do estudante que deseja atualizar?: '))

    query = 'SELECT count(1) AS c FROM estudantes WHERE id = ?'

    existe = defs_db.excute_query_fetchone(query, (atualizar,))

    if existe[0] > 0:

        print('1. Nome')
        print('2. CPF')
        qual = str(input('E qual dado deseja atualizar?: '))


        match qual:

            case '1':
                query = 'SELECT nome FROM estudantes WHERE id = ?'
                linha = defs_db.excute_query_fetchone(query, (atualizar, ))
                nome_novo = input(f'Qual será o nome novo do estudante {linha[0].capitalize()}?: ')
                dados = (nome_novo, atualizar)

                query = '''
                UPDATE estudantes SET nome = ? WHERE id = ?;
                '''

                defs_db.excute_query(query, dados)

            


            case '2':
                query = 'SELECT nome FROM estudantes WHERE id = ?'
                linha = defs_db.excute_query_fetchone(query, (atualizar,))

                while True:
                    try:
                        cpf_novo = int(input(f'Qual será o CPF novo do estudante {linha[0].capitalize()}?(apenas números, 11 caracteres): '))
                        if len(str(cpf_novo)) == 11:
                            break
                        else:
                            print('CPF inválido.', '\n')

                    except ValueError:
                        print('Digite apenas números inteiros.', '\n')

                dados = (cpf_novo, atualizar)
                query = '''
                UPDATE estudantes SET cpf = ? WHERE id = ?;
                '''
                defs_db.excute_query(query, dados)

            case _:
                print('Valor não encontrado')

    else: print('Estudante com esse ID não existe.')

    
            

def excluir_est(choose):

    print(f"Opção escolhida foi: {choose.capitalize()}")
    excluir = input('Qual o ID do estudante que deseja excluir?: ')

    query = 'select count(1) as c from estudantes where id = ?'

    existe = defs_db.excute_query_fetchone(query, (excluir, ))

    if existe[0] > 0:
        query = 'DELETE FROM matriculas WHERE estudante_id = ?'
        defs_db.excute_query(query, (excluir, ))

        query = 'DELETE FROM estudantes WHERE id = ?'
        defs_db.excute_query(query, (excluir, ))

    else:
        print(f'Nenhum estudante com o ID {excluir} foi encontrado.')


        

