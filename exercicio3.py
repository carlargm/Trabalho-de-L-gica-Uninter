print("Bem vindos a Fábrica de Roupas de Carla Regina Gomes Moreira Do Carmo")


# Exigência de código 2 de 7: Implementação da função escolha_modelo()
def escolha_modelo():
    while True:
        modelo = input("Escolha o modelo desejado (MCS/MLS/MCE/MLE): ").upper()
        if modelo in ["MCS", "MLS", "MCE", "MLE"]:
            # Retornar o valor do modelo com base na escolha do usuário
            if modelo == "MCS":
                return 1.80
            elif modelo == "MLS":
                return 2.10
            elif modelo == "MCE":
                return 2.90
            elif modelo == "MLE":
                return 3.20
        else:
            print("Opção de modelo inválida. Tente novamente.")

# Exigência de código 3 de 7: Implementação da função num_camisetas()
def num_camisetas():
    while True:
        try:
            num = int(input("Digite o número de camisetas desejado: "))
            if num < 20:
                desconto = 0
            elif num < 200:
                desconto = 5
            elif num < 2000:
                desconto = 7
            elif num <= 20000:
                desconto = 12
            else:
                print("Número de camisetas não pode ser maior que 20000.")
                continue
            
            # Calcular o número de camisetas com desconto
            num_com_desconto = num - (num * desconto / 100)
            
            return num_com_desconto
        
        except ValueError:
            print("Valor inválido. Digite um número válido.")

# Exigência de código 4 de 7: Implementação da função frete()
def frete():
    while True:
        try:
            opcao = int(input("Escolha o serviço adicional de frete (1 - Transportadora, 2 - Sedex, 0 - Retirar na fábrica): "))
            if opcao == 1:
                return 100
            elif opcao == 2:
                return 200
            elif opcao == 0:
                return 0
            else:
                print("Opção de frete inválida. Tente novamente.")
        
        except ValueError:
            print("Opção inválida. Digite 1, 2 ou 0.")

# Exigência de código 5 de 7: Implementação do cálculo total no código principal (main)
try:
    # Chamar as funções para obter as escolhas do usuário
    valor_modelo = escolha_modelo()
    qtd_camisetas = num_camisetas()
    valor_frete = frete()

    # Calcular o valor total a pagar
    total = (valor_modelo * qtd_camisetas) + valor_frete

    # Exigência de código 7 de 7: Comentários relevantes no código foram inseridos.

    # Exigência de saída de console 4 de 4: Apresentar um pedido com opções válidas
    print(f"Valor do modelo escolhido por unidade: R$ {valor_modelo:.2f}")
    print(f"Número de camisetas com desconto: {qtd_camisetas}")
    print(f"Valor do frete escolhido: R$ {valor_frete:.2f}")
    print(f"Total a pagar: R$ {total:.2f}")

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Exigência de saída de console 2 de 4: Apresentar um pedido em que o usuário errou a opção de modelo
# Simulação onde o usuário erra a opção de modelo inicialmente
print("\n--- Simulação onde o usuário erra a opção de modelo inicialmente ---")
escolha_modelo()

# Exigência de saída de console 3 de 4: Apresentar um pedido em que o usuário ultrapassa o número de camisetas
# Simulação onde o usuário ultrapassa o número máximo de camisetas aceitas
print("\n--- Simulação onde o usuário ultrapassa o número máximo de camisetas aceitas ---")
num_camisetas()

# Exigência de saída de console 1 de 4: Apresentar uma mensagem com meu nome completo
print("\n--- Mensagem com meu nome completo ---")
print("Bem-vindos à Fábrica de Camisetas do João Silva")
