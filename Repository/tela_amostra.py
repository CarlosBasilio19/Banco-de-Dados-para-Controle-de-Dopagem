import Amostra as am


while True:
    print("Menu de Opções")
    print("[1] - Listar Amostras")
    print("[2] - Buscar Amostras por ID")
    print("[3] - Buscar Amostras por Numero_CodigoDaAmostra")
    print("[4] - Inserir Amostra")
    print("[5] - Atualizar Amostra")
    print("[6] - Remover o Amostra")
    print("[0] - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        break
    elif opcao == 1:
        atletas = am.Listar_TodasAmostras()
        for atleta in atletas:
            print("\t",atleta,"\n")
    elif opcao == 2:
        id = input("Digite o ID do atleta: ")
        atleta = am.buscar_porID(id)
        print(atleta)
    elif opcao == 3:
        numero  = input("Informe o numero da amostra: ")
        atletas = am.busca_Numero_CodigoDaAmostra(numero)
        for atleta in atletas:
            print("\t",atleta)
    elif opcao == 4:
        id_amostra = input("Insira id_amostra")
        Numero_CodigoDaAmostra = input("Informe o Numero do Codigo Da Amostra ")
        InicialAtleta = input("Insira as iniciais dos Atleta")
        hora_selagem = input("Insira a hora da selagem")
        Numero_Amostra = input("Insira o Numero da Amostra")
        am.inserir(id_amostra,Numero_CodigoDaAmostra,InicialAtleta,hora_selagem, Numero_Amostra)
    elif opcao == 5:
        id_amostra = input("Insira id_amostra")
        Numero_CodigoDaAmostra = input("Informe o Numero do Codigo Da Amostra ")
        InicialAtleta = input("Insira as iniciais dos Atleta")
        hora_selagem = input("Insira a hora da selagem")
        Numero_Amostra = input("Insira o Numero da Amostra")
        am.atualizar(Numero_CodigoDaAmostra,InicialAtleta,hora_selagem,Numero_Amostra)
    elif opcao == 6:
        id = input("Informe o ID do atleta para remover: ")
        am.deletar(id)
        print("Removido com sucesso!")


