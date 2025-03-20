import Atleta as at

while True:
    print("Menu de Opções")
    print("[1] - Listar Atletas")
    print("[2] - Buscar Atleta por ID")
    print("[3] - Buscar Atleta por Nome")
    print("[4] - Inserir Atleta")
    print("[5] - Atualizar Atleta")
    print("[6] - Remover o Atleta")
    print("[0] - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        break
    elif opcao == 1:
        atletas = at.listar_todos()
        for atleta in atletas:
            print("\t",atleta,"\n")
    elif opcao == 2:
        id = input("Digite o ID do atleta: ")
        atleta = at.buscar_por_id(id)
        print(atleta)
    elif opcao == 3:
        nome = input("Informe o nome do atleta: ")
        atletas = at.buscar_por_nome(nome)
        for atleta in atletas:
            print("\t",atleta)
    elif opcao == 4:
        nome = input("Digite o nome do atleta: ")
        data_nascimento = input("Informe da data de nascimento do atleta(yyyy-mm-dd): ")
        at.inserir(nome,data_nascimento)
    elif opcao == 5:
        nome = input("Digite o nome do atleta: ")
        data_nascimento = input("Informe a data de nascimento: ")
        id = input("Informe o ID do atleta: ")
        at.atualizar(id,nome,data_nascimento)
    elif opcao == 6:
        id = input("Informe o ID do atleta para remover: ")
        at.deletar(id)
        print("Removido com sucesso!")