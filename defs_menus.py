import defs_atualizar
import defs_estudantes
import defs_disciplinas
import defs_professores
import defs_turmas

estudantes = []
disciplinas = []
professores = []
turmas = []
matriculas = []



def menu_geral(choose, menu):
    while choose != 'menu':
        print('\n')
        print(f"Menu {menu}")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        choose = str(input('Digite a opção desejada ou "Sair" para sair: '))
        choose = choose.lower()

        match menu:

            case 'estudantes':

                match choose:

                    case 'incluir' | '1':
                        choose = defs_estudantes.incluir_est(choose, estudantes)

                        
                    case 'listar' | '2':
                        choose = defs_estudantes.listar_est(choose, estudantes)


                    case 'atualizar' | '3':
                        choose = defs_estudantes.atualizar_est(choose, estudantes)


                    case 'excluir' | '4':
                        choose = defs_estudantes.excluir_est(choose, estudantes)
                        

                    case 'sair':
                        break

                    case _:
                        continue

                 




            case 'disciplinas':
                
                match choose:

                    case 'incluir' | '1':
                        choose = defs_disciplinas.incluir_disciplina(choose, disciplinas)

                    case 'listar' | '2':
                        choose = defs_disciplinas.listar_disciplina(choose, disciplinas)

                    case 'atualizar' | '3':
                        choose = defs_disciplinas.atualizar_disciplina(choose, disciplinas)

                    case 'excluir' | '4':
                        choose = defs_disciplinas.excluir_disciplinas(choose, disciplinas)

                    case 'sair':
                        break

                    case _:
                        continue
            case 'professores':
                
                match choose:

                    case 'incluir' | '1':
                        choose = defs_professores.incluir_prof(choose, professores)  

                    case 'listar' | '2':
                        choose = defs_professores.listar_prof(choose, professores)  

                    case 'atualizar' | '3':
                        choose = defs_professores.atualizar_prof(choose, professores)  

                    case 'excluir' | '4':
                        choose = defs_professores.excluir_prof(choose, professores)  

                    case 'sair':
                        break

                    case _:
                        continue
            case 'turmas':
                
                match choose:

                    case 'incluir' | '1':
                        choose = defs_turmas.incluir_turma(choose, turmas)

                    case 'listar' | '2':
                        choose = defs_turmas.listar_turma(choose, turmas)

                    case 'atualizar' | '3':
                        choose = defs_turmas.atualizar_turma(choose, turmas)

                    case 'excluir' | '4':
                        choose = defs_turmas.excluir_turma(choose, turmas)

                    case 'sair':
                        break

                    case _:
                        continue

            case 'matriculas':

                match choose:

                    case 'incluir' | '1':
                        print(f"Opção escolhida foi: {choose.capitalize()}")
                        continue  

                    case 'listar' | '2':
                        print(f"Opção escolhida foi: {choose.capitalize()}")
                        continue

                    case 'atualizar' | '3':
                        print(f"Opção escolhida foi: {choose.capitalize()}")
                        continue

                    case 'excluir' | '4':
                        print(f"Opção escolhida foi: {choose.capitalize()}")
                        continue

                    case 'sair':
                        break

                    case _:
                        continue

    return choose   

        
                # match choose:
                #     case 'incluir' | '1':
                #         print(f"Opção escolhida foi: {choose.capitalize()}")
                #         continue  

                #     case 'listar' | '2':
                #         print(f"Opção escolhida foi: {choose.capitalize()}")
                #         continue

                #     case 'atualizar' | '3':
                #         print(f"Opção escolhida foi: {choose.capitalize()}")
                #         continue

                #     case 'excluir' | '4':
                #         print(f"Opção escolhida foi: {choose.capitalize()}")
                #         continue

                #     case 'sair':
                #         break

                #     case _:
                #         continue

#     return choose

# def menu_professores(choose):
#     while choose != 'menu':
#         print('\n')
#         print("Menu Professores")
#         print("1. Incluir")
#         print("2. Listar")
#         print("3. Atualizar")
#         print("4. Excluir")
#         choose = str(input('Digite a opção desejada ou "Sair" para sair: '))
#         choose = choose.lower()
#         if choose == 'incluir' or choose == '1':
#             print(f"Opção escolhida foi: {choose.capitalize()}")
#             continue
#         elif choose == 'listar' or choose == '2':
#             print(f"Opção escolhida foi: {choose.capitalize()}")
#             continue
#         elif choose == 'atualizar' or choose == '3':
#             print(f"Opção escolhida foi: {choose.capitalize()}")
#             continue
#         elif choose == 'excluir' or choose == '4':
#             print(f"Opção escolhida foi: {choose.capitalize()}")
#             continue
#         elif choose == 'sair':
#             break
#         else:
#             continue

# def menu_turmas(choose):
#     while choose != 'menu':
#         print('\n')
#         print("Menu Turmas")
#         print("1. Incluir")
#         print("2. Listar")
#         print("3. Atualizar")
#         print("4. Excluir")
#         choose = str(input('Digite a opção desejada ou "Sair" para sair: '))
#         choose = choose.lower()
#         if choose == 'incluir' or choose == '1':
#             print(f"Opção escolhida foi: {choose.capitalize()}")
#             continue
#         elif choose == 'listar' or choose == '2':
#             print(f"Opção escolhida foi: {choose.capitalize()}")
#             continue
#         elif choose == 'atualizar' or choose == '3':
#             print(f"Opção escolhida foi: {choose.capitalize()}")
#             continue
#         elif choose == 'excluir' or choose == '4':
#             print(f"Opção escolhida foi: {choose.capitalize()}")
#             continue
#         elif choose == 'sair':
#             break
#         else:
#             continue
     
# def menu_matriculas(choose):
#     while choose != 'menu':
#         print('\n')
#         print("Menu Matriculas")
#         print("1. Incluir")
#         print("2. Listar")
#         print("3. Atualizar")
#         print("4. Excluir")
#         choose = str(input('Digite a opção desejada ou "Sair" para sair: '))
#         choose = choose.lower()
#         if choose == 'incluir' or choose == '1':
#             print(f"Opção escolhida foi: {choose.capitalize()}")
#             continue
#         elif choose == 'listar' or choose == '2':
#             print(f"Opção escolhida foi: {choose.capitalize()}")
#             continue
#         elif choose == 'atualizar' or choose == '3':
#             print(f"Opção escolhida foi: {choose.capitalize()}")
#             continue
#         elif choose == 'excluir' or choose == '4':
#             print(f"Opção escolhida foi: {choose.capitalize()}")
#             continue
#         elif choose == 'sair':
#             break
#         else:
#             continue