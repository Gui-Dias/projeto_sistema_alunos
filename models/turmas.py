import defs_atualizar


def incluir_turma(choose):
    print(f"Opção escolhida foi: {choose.capitalize()}")

    try:
        id = int(input('Digite o ID da turma (apenas numeros): '))
 
        periodo = int(input(f'Em qual periodo esta turma está? (1 - 12): '))

        disciplina_turma = input('Qual a disciplina dessa turma?: ')


        verifier = False
        for turma in turmas:
            if id == turma['id']:
                verifier = True

        if verifier:
            print('\n', "Uma disciplina com esse id ja foi cadastrada, informe outro.")

        else:
            turmas.append({'id': id, 'disciplina': disciplina_turma, 'periodo': periodo})
            print('\n')
            print(f"Turma de {disciplina_turma} do {periodo} periodo adicionada.")

    except ValueError:
        print('Tipo de dado inserido não é válido')


def listar_turma(choose):
    print(f"Opção escolhida foi: {choose.capitalize()}")

    if turmas:
        print("Lista de turmas: ")
        for turma in turmas:
            print(f'--Disciplina: {turma['disciplina']} | ID: {turma['id']} | Periodo: {turma['periodo']}')

    else: print('\n','Nenhuma turma cadastrada.')


def atualizar_turma(choose):
    print(f"Opção escolhida foi: {choose.capitalize()}")
    atualizar = input('Qual o ID da disciplina que deseja atualizar?: ')
    print('\n')
    indice = defs_atualizar.pegarid_turmas (turmas, atualizar)
    if indice:
        print('E qual dado deseja atualizar?')
        print('1. ID')
        print('2. Disciplina')
        print('3. Duração')
        qual = str(input('E qual dado deseja atualizar?: '))

        match qual:

            case '1' | 'id':
                defs_atualizar.id_turmas(turmas, indice)

            case '2' | 'disciplina':
                defs_atualizar.turma_disciplina_edit(turmas, indice)

            case '3' | 'duração' | 'duracao':
                defs_atualizar.periodo_edit(turmas, indice)

            case _:
                print('Valor não encontrado')
            

def excluir_turma(choose):
    try:
        print(f"Opção escolhida foi: {choose.capitalize()}")
        excluir = int(input('Qual o ID da turma que deseja excluir?: '))
        encontrou = None
        for turma in turmas:
            if excluir == turma['id']:
                turmas.remove(turma)
                encontrou = True
                break

        if not encontrou:
            print(f'Nenhuma disciplina com o ID {excluir} foi encontrado.: ')

    except ValueError:
        print("Digite apenas números")
            

