excelente = 0
ruim = 0

for i in range(50):
    print(f"\nEntrevistado {i + 1}")

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    print("Como você avalia o atendimento?")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opção: "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

print("\n===== RESULTADO DA PESQUISA =====")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")