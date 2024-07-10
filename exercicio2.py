# Exigência de código 1 de 8: Implementação do print com meu nome completo e o menu.
print("Bem-vindos à loja de Carla Regina Gomes Moreira Do Carmo")
print("""
Menu:
1. Bife Acebolado (BA)
    - Tamanho P: R$ 16
    - Tamanho M: R$ 18
    - Tamanho G: R$ 22
2. Filé de Frango (FF)
    - Tamanho P: R$ 15
    - Tamanho M: R$ 17
    - Tamanho G: R$ 21
""")

# Exigência de código 5 de 8: Implementação de um acumulador para somar os valores dos pedidos.
total = 0

while True:
    # Loop para garantir que o sabor seja corretamente informado
    while True:
        sabor = input("Digite o sabor (BA/FF): ").upper()
        if sabor not in ["BA", "FF"]:
            print("Sabor inválido. Tente novamente.")
            continue
        break

    # Loop para garantir que o tamanho seja corretamente informado
    while True:
        tamanho = input("Digite o tamanho (P/M/G): ").upper()
        if tamanho not in ["P", "M", "G"]:
            print("Tamanho inválido. Tente novamente.")
            continue
        break

    # Exigência de código 4 de 8: Implementação de if-elif-else aninhado para determinar o preço.
    if sabor == "BA":
        if tamanho == "P":
            preco = 16
        elif tamanho == "M":
            preco = 18
        elif tamanho == "G":
            preco = 22
    elif sabor == "FF":
        if tamanho == "P":
            preco = 15
        elif tamanho == "M":
            preco = 17
        elif tamanho == "G":
            preco = 21

    print(f"Você pediu uma marmita de {sabor} tamanho {tamanho} que custa R$ {preco}")

    # Exigência de código 5 de 8: Acumulador para somar os valores dos pedidos.
    total += preco

    # Exigência de código 6 de 8: Perguntar se deseja pedir mais alguma coisa.
    while True:
        mais = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
        if mais not in ["S", "N"]:
            print("Opção inválida. Tente novamente.")
            continue
        break

    if mais == "N":
        break

# Exibir o total acumulado.
print(f"Total do pedido: R$ {total:.2f}")

# Exigência de código 8 de 8: Comentários relevantes no código foram inseridos.
