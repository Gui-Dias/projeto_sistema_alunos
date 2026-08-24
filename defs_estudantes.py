import defs_atualizar
import defs_matricula
import sqlite3

def incluir_est(choose, estudantes):
    conexao = sqlite3.connect('sistema_alunos/main.db')
    cursor = conexao.cursor()
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

    cursor.execute('''
    INSERT INTO estudantes (nome, cpf) VALUES (?, ?);
    ''', dados)
    id_gerado = cursor.lastrowid
    conexao.commit()
    print(f"Estudante {nomeadd} de id {id_gerado} adicionado.")
    conexao.close


    matricula = defs_matricula.gerador_matricula()

    matricula_id = (matricula, id_gerado)

    conexao = sqlite3.connect('sistema_alunos/main.db')

    cursor = conexao.cursor()
    cursor.execute('''
    INSERT INTO matriculas (matricula, estudante_id) VALUES (?, ?);
    ''', matricula_id)
    conexao.commit()
    conexao.close()





def listar_est(choose, estudantes):
    
    print(f"Opção escolhida foi: {choose.capitalize()}")
    print("Lista de estudantes: ")
    conexao = sqlite3.connect('sistema_alunos/main.db')
    cursor = conexao.cursor()

    query = """
        SELECT e.id, e.nome, e.cpf, m.matricula 
        FROM estudantes e
        INNER JOIN matriculas m ON e.id = m.estudante_id
    """
    
    cursor.execute(query)
    resultados = cursor.fetchall()

    for row in resultados:
        estudante_id = row[0]
        nome_estudante = row[1]
        nome_estudante = nome_estudante.capitalize()
        cpf_estudante = row[2]
        matricula_atual = row[3]

        
        print(f'ID: {estudante_id} | Nome: {nome_estudante} | CPF: {cpf_estudante} | Matricula: {matricula_atual}')

    conexao.close()





def atualizar_est(choose, estudantes):
    print(f"Opção escolhida foi: {choose.capitalize()}")
    atualizar = int(input('Qual o ID do estudante que deseja atualizar?: '))
    conexao = sqlite3.connect('sistema_alunos/main.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT count(1) AS c FROM estudantes WHERE id = ?', (atualizar, ))
    existe = cursor.fetchone()

    if existe[0] > 0:

        print('1. Nome')
        print('2. CPF')
        qual = str(input('E qual dado deseja atualizar?: '))


        match qual:

            case '1':
                cursor.execute('SELECT nome FROM estudantes WHERE id = ?', (atualizar,))
                linha = cursor.fetchone()
                nome_novo = input(f'Qual será o nome novo do estudante {linha[0].capitalize()}?: ')
                dados = (nome_novo, atualizar)
                cursor.execute('''
                UPDATE estudantes SET nome = ? WHERE id = ?;
                ''', dados)
                conexao.commit()
                conexao.close()
            


            case '2':
                cursor.execute('SELECT nome FROM estudantes WHERE id = ?', (atualizar,))
                linha = cursor.fetchone()

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
                cursor.execute('''
                UPDATE estudantes SET cpf = ? WHERE id = ?;
                ''', dados)
                conexao.commit()
                conexao.close()

            case _:
                print('Valor não encontrado')

    else: print('Estudante com esse ID não existe.')

    conexao.close()
    
            

def excluir_est(choose, estudantes):
    conexao = sqlite3.connect('sistema_alunos/main.db')
    cursor = conexao.cursor()
    print(f"Opção escolhida foi: {choose.capitalize()}")
    excluir = input('Qual o ID do estudante que deseja excluir?: ')

    cursor.execute('select count(1) as c from estudantes where id = ?',(excluir, ))
    existe = cursor.fetchone()

    if existe[0] > 0:
        cursor.execute('DELETE FROM matriculas WHERE estudante_id = ?', (excluir, ))
        cursor.execute('DELETE FROM estudantes WHERE id = ?', (excluir, ))
        conexao.commit()

    else:
        print(f'Nenhum estudante com o ID {excluir} foi encontrado.')

    conexao.close()
        

