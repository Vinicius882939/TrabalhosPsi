# Sistema de Gestão de Nomes

nomes = []

while True:
    print("\n--- MENU ---")
    print("1. Adicionar nome")
    print("2. Remover nome")
    print("3. Listar todos os nomes")
    print("4. Procurar um nome")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    # 1. Adicionar nome
    if opcao == "1":
        nome = input("Digite o nome a adicionar: ").strip()
        nomes.append(nome)
        print("Nome adicionado com sucesso!")

    # 2. Remover nome
    elif opcao == "2":
        nome = input("Digite o nome a remover: ").strip().lower()
        removido = False

        for n in nomes:
            if n.lower() == nome:
                nomes.remove(n)
                removido = True
                break

        if removido:
            print("Nome removido com sucesso!")
        else:
            print("Nome não encontrado.")

    # 3. Listar nomes
    elif opcao == "3":
        if len(nomes) == 0:
            print("Nenhum nome cadastrado.")
        else:
            print("Lista de nomes:")
            for n in nomes:
                print("-", n)

    # 4. Procurar nome
    elif opcao == "4":
        nome = input("Digite o nome a procurar: ").strip().lower()
        encontrado = False

        for n in nomes:
            if n.lower() == nome:
                encontrado = True
                break

        if encontrado:
            print("Nome encontrado!")
        else:
            print("Nome não encontrado.")

    # 5. Sair
    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")


