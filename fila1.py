# Entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
gestante = input("É gestante? (s/n): ").lower() == "s"
pcd = input("É pessoa com deficiência (pcd)? (s/n): ").lower() == "s"

# Lógica booleana para prioridade
if idade >= 60 or gestante or pcd:
    print("PRIORITÁRIO")
else:
    print("NORMAL")
