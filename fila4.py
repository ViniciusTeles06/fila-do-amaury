# Fila feita por vinicius Telles

# Listas para armazenar as pessoas em cada fila e os atendidos
fila_prioritaria = []
fila_normal = []
atendidos = []

# Função para adicionar uma pessoa à fila
def adicionar():
    nome = input("Nome: ")
    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Idade inválida!\n")
        return
    # Pergunta se é gestante e se é PCD
    gestante = input("É gestante? (s/n): ").lower() == "s"
    pcd = input("É pessoa com deficiência (pcd)? (s/n): ").lower() == "s"
    # Define se a pessoa é prioritária
    prioritario = idade >= 60 or gestante or pcd
    pessoa = {
        "nome": nome,
        "idade": idade,
        "gestante": gestante,
        "pcd": pcd,
        "prioritario": prioritario
    }
    # Adiciona na fila correta
    if prioritario:
        fila_prioritaria.append(pessoa)
        print("Adicionado na fila prioritária!\n")
    else:
        fila_normal.append(pessoa)
        print("Adicionado na fila normal!\n")

# Função para atender a próxima pessoa (priorizando a fila prioritária)
def atender():
    if fila_prioritaria:
        pessoa = fila_prioritaria.pop(0)
        print(f"Atendido (prioritário): {pessoa['nome']}\n")
    elif fila_normal:
        pessoa = fila_normal.pop(0)
        print(f"Atendido (normal): {pessoa['nome']}\n")
    else:
        print("Nenhuma pessoa na fila!\n")
        return
    atendidos.append(pessoa)

# Função para listar as pessoas nas filas
def listar():
    print("\nFila prioritária:")
    if fila_prioritaria:
        for p in fila_prioritaria:
            print(f"{p['nome']} - Idade: {p['idade']} - Gestante: {'Sim' if p['gestante'] else 'Não'} - PCD: {'Sim' if p['pcd'] else 'Não'}")
    else:
        print("Vazia.")
    print("\nFila normal:")
    if fila_normal:
        for p in fila_normal:
            print(f"{p['nome']} - Idade: {p['idade']} - Gestante: {'Sim' if p['gestante'] else 'Não'} - PCD: {'Sim' if p['pcd'] else 'Não'}")
    else:
        print("Vazia.")
    print()

# Função para mostrar um relatório de atendimentos e filas
def relatorio():
    total_atendidos = len(atendidos)
    prio_atendidos = sum(1 for p in atendidos if p['prioritario'])
    total_fila = len(fila_prioritaria) + len(fila_normal)
    prio_fila = len(fila_prioritaria)
    print(f"\nRelatório:")
    print(f"Atendidos: {total_atendidos} (Prioritários: {prio_atendidos})")
    print(f"Na fila: {total_fila} (Prioritários: {prio_fila})")
    if total_atendidos > 0:
        print(f"% Prioritários atendidos: {100 * prio_atendidos / total_atendidos:.1f}%")
    else:
        print("% Prioritários atendidos: 0%")
    print()

# Função principal do menu
def menu():
    while True:
        print("1) Adicionar cliente")
        print("2) Atender próximo")
        print("3) Listar filas")
        print("4) Relatório")
        print("5) Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar()
        elif opcao == "2":
            atender()
        elif opcao == "3":
            listar()
        elif opcao == "4":
            relatorio()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

# Inicia o programa chamando o menu
menu()
