def pegarid_estudantes(estudantes, atualizar):
    indice = -1
    for estudante in estudantes:
        if estudante['id'] == atualizar:
            indice = estudantes.index(estudante)

    if indice >= 0:
        return indice
    else:
        print(f'Nenhum estudante com o id {atualizar} foi encontrado.')
        return indice

    
def idedit(estudantes, indice):
    idnovo = input(f'Qual será o id novo do estudante {estudantes[indice]['nome']}?: ')
    verifier = 0
    for estudante in estudantes:
        if idnovo == estudante['id']:
            verifier += 1

    if verifier != 0:
        print('\n', "Estudante com esse id ja foi cadastrado, informe outro.")

    else:
        estudantes[indice]['id'] = idnovo

def nomeedit(estudantes, indice):
    nomenovo = input(f'Qual será o nome novo do estudante {estudantes[indice]['nome']}?: ')
    estudantes[indice]['nome'] = nomenovo

def cpfedit(estudantes, indice):
    cpfnovo = input(f'Qual será o nome novo do estudante {estudantes[indice]['nome']}?: ')
    estudantes[indice]['cpf'] = cpfnovo

# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------

def pegarid_disciplinas(disciplinas, atualizar):
    indice = -1

    for disciplina in disciplinas:
        if disciplina['id'] == atualizar:
            indice = disciplinas.index(disciplina)

    if indice >= 0:
        return indice
    else:
        print(f'Nenhuma disciplina com o id {atualizar} foi encontrado.')
    
def id_disciplinas_edit(disciplinas, indice):
    idnovo = input(f'Qual será o id atualizado da disciplina {disciplinas[indice]['disciplina']}?: ')
    verifier = 0
    for disciplina in disciplinas:
        if idnovo == disciplina['id']:
            verifier += 1

    if verifier != 0:
        print('\n', "Estudante com esse id ja foi cadastrado, informe outro.")

    else:
        disciplinas[indice]['id'] = idnovo

def disciplina_edit(disciplinas, indice):
    nomenovo = input(f'Qual será o nome atualizado da disciplina {disciplinas[indice]['disciplina']}?: ')
    disciplinas[indice]['disciplina'] = nomenovo

def area_edit(disciplinas, indice):
    print('1. Humanas')
    print('2. Exatas')
    print('3. Ambas')
    area_nova = input(f'Qual será a área atualizada da disciplina {disciplinas[indice]['disciplina']}?: ')

    match area_nova:

        case '1' | 'humanas':
            disciplinas[indice]['area'] = 'Humanas'

        case '2' | 'exatas':
            disciplinas[indice]['area'] = 'Exatas'
            
        case '3' | 'ambas':
            disciplinas[indice]['area'] = 'Humanas e Exatas'

# ----------------------------------------------------------------------------------------------------------------    
# ----------------------------------------------------------------------------------------------------------------


def pegarid_professores(professores, atualizar):
    indice = -1

    for professor in professores:
        if professor['id'] == atualizar:
            indice = professores.index(professor)

    if indice >= 0:
        return indice
    else:
        print(f'Nenhum professor com o id {atualizar} foi encontrado.')
    
def id_professores_edit(professores, indice):
    idnovo = input(f'Qual será o id atualizado do professor {professores[indice]['nome']}?: ')
    verifier = 0
    for professor in professores:
        if idnovo == professor['id']:
            verifier += 1

    if verifier != 0:
        print('\n', "Estudante com esse id ja foi cadastrado, informe outro.")

    else:
        professores[indice]['id'] = idnovo

def professor_edit(professores, indice):
    nomenovo = input(f'Qual será o nome atualizado do professor {professores[indice]['nome']}?: ')
    professores[indice]['nome'] = nomenovo

def area_edit(professores, indice):
    print('1. Humanas')
    print('2. Exatas')
    print('3. Ambas')
    duracao_nova = input(f'Qual será a área de atuação atualizada do professor {professores[indice]['nome']}?: ')

    match duracao_nova:

        case '1' | 'humanas':
            professores[indice]['area'] = 'Humanas'

        case '2' | 'exatas':
            professores[indice]['area'] = 'Exatas'
            
        case '3' | 'ambas':
            professores[indice]['area'] = 'Humanas e Exatas'


# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------

def pegarid_turmas(turmas, atualizar):
    indice = None
    for turma in turmas:
        if turma['id'] == atualizar:
            indice = turmas.index(turma)

    if indice:
        return indice
    else:
        print(f'Nenhuma turma com o id {atualizar} foi encontrado.')
        return indice

    
def id_turmas(turmas, indice):
    idnovo = input(f'Qual será o id novo da turma {turmas[indice]['disciplina']}?: ')
    verifier = 0
    for turma in turmas:
        if idnovo == turma['id']:
            verifier += 1

    if verifier != 0:
        print('\n', "Estudante com esse id ja foi cadastrado, informe outro.")

    else:
        turmas[indice]['id'] = idnovo

def turma_disciplina_edit(turmas, indice):
    nomenovo = input(f'Qual será a disciplina nova da turma de {turmas[indice]['disciplina']}?: ')
    turmas[indice]['disciplina'] = nomenovo

def periodo_edit(turmas, indice):
    periodo = input(f'Qual será periodo atualizado da turma de {turmas[indice]['disciplina']}?: ')
    turmas[indice]['periodo'] = periodo