pessoas = []
n = int(input("Quantas pessoas deseja cadastrar? "))

for i in range(n):
    nome = input(f"Nome da pessoa {i+1}: ")
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

# Contagem
qtd_prio = sum(1 for p in pessoas if p["prioritario"])
qtd_n_prio = len(pessoas) - qtd_prio

print(f"\nTotal prioritários: {qtd_prio}")
print(f"Total não prioritários: {qtd_n_prio}")

# Remover a primeira pessoa não prioritária (se existir)
for i, p in enumerate(pessoas):
    if not p["prioritario"]:
        removida = pessoas.pop(i)
        print(f"\nRemovida a primeira pessoa não prioritária: {removida['nome']}")
        break
else:
    print("\nNão havia pessoas não prioritárias para remover.")

# Mostrar lista final
print("\nLista final de pessoas:")
for p in pessoas:
    print(f"{p['nome']} - Prioritário: {'Sim' if p['prioritario'] else 'Não'}")
