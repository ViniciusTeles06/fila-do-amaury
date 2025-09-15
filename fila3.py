pessoas = []

def adicionar():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    gestante = input("É gestante? (s/n): ").lower() == "s"
    pcd = input("É pessoa com deficiência (pcd)? (s/n): ").lower() == "s"
    prioritario = idade >= 60 or gestante or pcd
    pessoa = {
        "nome": nome,
        "idade": idade,
        "gestante": gestante,
        "pcd": pcd,
        "prioritario": prioritario
    }
    pessoas.append(pessoa)
    print("Pessoa adicionada!\n")

def listar():
    if not pessoas:
        print("Nenhuma pessoa cadastrada.\n")
        return
    print("\nLista de pessoas:")
    for p in pessoas:
        print(f"{p['nome']} - Prioritário: {'Sim' if p['prioritario'] else 'Não'}")
    print()

def menu():
    while True:
        print("1) Adicionar pessoa")
        print("2) Listar pessoas")
        print("3) Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

menu()
