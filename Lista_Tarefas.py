# Projeto Final - Curso Python Diversifica.Dev
# Autora: Gabryelle Peixer
# Lista de Tarefas

def exibir_menu():
    print("=" * 69)
    print("\n---- MENU PRINCIPAL ----\n") 
    print("O que vamos fazer hoje?\n"
          "1. Adicionar tarefa\n"
          "2. Remover tarefa\n"
          "3. Ver tarefas\n"
          "4. Sair\n"
          )
    
def add_tarefa(lista_de_tarefas, tarefa):
    lista_de_tarefas.append(tarefa)
    print(f"Tarefa adicionada com sucesso!")
    return lista_de_tarefas

def listar_tarefas (lista_de_tarefas):
    print("-" * 40)
    print("Tarefas atuais:")
    n = 1
    for tarefa in lista_de_tarefas:
        print(f"{n} - {tarefa}")
        n += 1
    print("-" * 40)

def rem_tarefa (lista_de_tarefas, tarefa):
    lista_de_tarefas.pop((tarefa - 1))
    return lista_de_tarefas

lista_de_tarefas = []
continuar = True

while continuar:
    exibir_menu()
    opcao = input("Insira a opção desejada (apenas número): ")
    if opcao == "1":
        tarefa = input("Insira a nova tarefa: ")
        lista_de_tarefas = add_tarefa(lista_de_tarefas, tarefa)
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
        continuar = False
    else:
        print("Opção inválida, por favor, tente novamente, inserindo o número da opção desejada.")
