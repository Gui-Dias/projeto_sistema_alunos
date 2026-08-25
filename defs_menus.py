import defs_atualizar
import models.estudantes as estudantes
import models.disciplinas
import models.professores
import models.turmas as turmas


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
                        choose = estudantes.incluir_est(choose)

                        
                    case 'listar' | '2':
                        choose = estudantes.listar_est(choose)


                    case 'atualizar' | '3':
                        choose = estudantes.atualizar_est(choose)


                    case 'excluir' | '4':
                        choose = estudantes.excluir_est(choose)
                        

                    case 'sair':
                        break

                    case _:
                        continue

                 




            case 'disciplinas':
                
                match choose:

                    case 'incluir' | '1':
                        choose = disciplinas.incluir_disciplina(choose, disciplinas)

                    case 'listar' | '2':
                        choose = disciplinas.listar_disciplina(choose, disciplinas)

                    case 'atualizar' | '3':
                        choose = disciplinas.atualizar_disciplina(choose, disciplinas)

                    case 'excluir' | '4':
                        choose = disciplinas.excluir_disciplinas(choose, disciplinas)

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
                        choose = turmas.incluir_turma(choose, turmas)

                    case 'listar' | '2':
                        choose = turmas.listar_turma(choose, turmas)

                    case 'atualizar' | '3':
                        choose = turmas.atualizar_turma(choose, turmas)

                    case 'excluir' | '4':
                        choose = turmas.excluir_turma(choose, turmas)

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