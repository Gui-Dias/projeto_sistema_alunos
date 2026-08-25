import defs_atualizar
import sqlite3

def incluir_prof(choose, professores):
    conexao = sqlite3.connect('main.db')
    cursor = conexao.cursor()
    print(f"Opção escolhida foi: {choose.capitalize()}")

    nomeadd = input('Digite o nome do professor: ')
    nomeadd = nomeadd.capitalize()

    print('1. Humanas')
    print('2. Exatas')
    print('3. Ambas')
    areaadd = input('Qual área esse professor atua?: ')

    verifier = 0
    for professor in professores:
        if idadd == professor['id']:
            verifier += 1

    if verifier != 0:
        print('\n', "Professor com esse id ja foi cadastrado, informe outro.")

    else:
        match areaadd:

            case '1' | 'humanas':
                professores.append({'id': idadd, 'nome': nomeadd, 'area': 'Humanas'})
                print('\n')
                print(f"Professor {nomeadd} adicionado.")

            case '2' | 'exatas':
                professores.append({'id': idadd, 'nome': nomeadd, 'area': 'Exatas'})
                print('\n')
                print(f"Professor {nomeadd} adicionado.")

            case '3' | 'ambas':
                professores.append({'id': idadd, 'nome': nomeadd, 'area': 'Humanas e Exatas'})
                print('\n')
                print(f"Professor {nomeadd} adicionado.")


def listar_prof(choose, professores):
    print(f"Opção escolhida foi: {choose.capitalize()}")
    print("Lista de professores: ")
    for professor in professores:
        print(f'--Nome: {professor['nome']} | ID: {professor['id']} | Área de atuação: {professor['area']}')


def atualizar_prof(choose, professores):
    print(f"Opção escolhida foi: {choose.capitalize()}")
    atualizar = input('Qual o ID do professor que deseja atualizar?: ')
    indice = defs_atualizar.pegarid_professores(professores, atualizar)
    print('1. ID')
    print('2. Nome')
    print('3. Área de atuação')
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
            

def excluir_prof(choose, professores):
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
        

