# Projeto Final - Curso Python Diversifica.Dev
# Autora: Gabryelle Peixer
# Lista de Tarefas

def exibir_menu(): #Exibe o menu principal
    print("=" * 69)
    print("\n---- MENU PRINCIPAL ----\n") 
    print("O que vamos fazer hoje?\n"
          "1. Adicionar tarefa\n"
          "2. Remover tarefa\n"
          "3. Ver tarefas\n"
          "4. Sair\n"
          )
    
def add_tarefa(lista_de_tarefas, tarefa): #Adiciona uma nova tarefa à lista
    lista_de_tarefas.append(tarefa)
    print(f"Tarefa adicionada com sucesso!")
    return lista_de_tarefas

def add_horario(lista_de_horarios, horario): #Adiciona um horário à tarefa
    lista_de_horarios.append(horario)
    return lista_de_horarios

def listar_tarefas (lista_de_tarefas): #Lista todas as tarefas atuais e seus horários
    print("-" * 40)
    print(f"{' ' * 15}""Tarefas atuais:")
    n = 1
    for n, (tarefa, horario) in enumerate(zip(lista_de_tarefas, lista_de_horarios), 1):
        print(f"{n} - {tarefa} - Horário: {horario}")
        n += 1
    print("-" * 40)

def rem_tarefa (lista_de_tarefas, tarefa): #Remove uma tarefa da lista
    lista_de_tarefas.pop((tarefa - 1))
    return lista_de_tarefas

lista_de_tarefas = []
lista_de_horarios = []
continuar = True

while continuar:
    exibir_menu()
    opcao = input("Insira a opção desejada (apenas número): ")
    if opcao == "1":
        tarefa = input("Insira a nova tarefa: ").capitalize()
        resposta = input("Deseja definir um horário para a tarefa? (s/n): ").lower()
        if resposta == "s":
            horario = input("Insira o horário para a tarefa: ").capitalize()
        elif resposta == "n":
            horario = "Não definido"
        else:
            print("Resposta inválida! Retornando ao menu principal...")
            continue

        add_tarefa(lista_de_tarefas, tarefa)
        add_horario(lista_de_horarios, horario)

    elif opcao == "2":
        tarefa = (input("Insira a tarefa que deseja remover (apenas números): "))
        if not tarefa.isnumeric():
            print("Valor inválido! Esta função apenas aceita números!")
        elif int(tarefa) > len(lista_de_tarefas):
            print("Número inválido! Selecione um número de tarefa válido!")
        elif int(tarefa) <= 0:
            print("Número inválido! Selecione um número de tarefa válido!")
        else:
            lista_de_tarefas = rem_tarefa(lista_de_tarefas, int(tarefa))
            print("Tarefa removida com sucesso! Lista atualizada abaixo!")
            listar_tarefas(lista_de_tarefas)
    elif opcao == "3":
        listar_tarefas(lista_de_tarefas)
    elif opcao == "4":
        print("\n")
        print("Aqui está sua lista final de tarefas!\n")
        listar_tarefas(lista_de_tarefas)
        print("\nObrigada por usar o programa! Até a próxima! ^^\n")
        continuar = False
    else:
        print("Opção inválida, por favor, tente novamente, inserindo o número da opção desejada.")
