import defs_menus

choose = ''
while choose != 'sair':
    print('\n')
    print(f"Menu principal")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matrículas")
    choose = str(input('Digite a opção desejada ou "Sair" para sair: '))
    choose = choose.lower()

    match choose:

        case '1' | 'estudantes':
            menu = 'estudantes'
            choose = defs_menus.menu_geral(choose, menu)


        case '2' | 'disciplinas':
            menu = 'disciplinas'
            choose = defs_menus.menu_geral(choose, menu)


        case '3' | 'professores':
            menu = 'professores'
            choose = defs_menus.menu_geral(choose, menu)
            

        case '4' | 'turmas':
            menu = 'turmas'
            choose = defs_menus.menu_geral(choose, menu)


        case '5' | 'matriculas':
            menu = 'matriculas'
            choose = defs_menus.menu_geral(choose, menu)

        case 'sair':
            break