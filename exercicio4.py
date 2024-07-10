# A. Print com nome completo
print("Bem vindos à empresa de Carla Regina Gomes Moreira Do Carmo")

# B. Lista de funcionários e variável id_global
lista_funcionarios = []
id_global = 4687087 # Valor inicial baseado no número do RU

# C. Função para cadastrar funcionário
def cadastrar_funcionario(id):
    global id_global  # Acessa a variável global id_global
    
    # Pergunta os dados do funcionário
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    
    # Cria um dicionário com os dados do funcionário
    funcionario = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }
    
    # Adiciona o funcionário à lista de funcionários
    lista_funcionarios.append(funcionario.copy())  # Utiliza .copy() para evitar referências indesejadas
    
    # Incrementa o id_global para o próximo funcionário
    id_global += 1

# D. Função para consultar funcionários
def consultar_funcionarios():
    while True:
        print("\nMenu Consultar Funcionário:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            # Consultar todos os funcionários
            if not lista_funcionarios:
                print("Nenhum funcionário cadastrado.")
            else:
                print("\nFuncionários Cadastrados:")
                for funcionario in lista_funcionarios:
                    print(f"ID: {funcionario['id']}, Nome: {funcionario['nome']}, Setor: {funcionario['setor']}, Salário: R$ {funcionario['salario']}")
        
        elif opcao == "2":
            # Consultar por Id
            id_consulta = int(input("Digite o ID do funcionário: "))
            encontrado = False
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_consulta:
                    print(f"\nFuncionário encontrado:")
                    print(f"ID: {funcionario['id']}, Nome: {funcionario['nome']}, Setor: {funcionario['setor']}, Salário: R$ {funcionario['salario']}")
                    encontrado = True
                    break
            if not encontrado:
                print("Funcionário não encontrado.")
        
        elif opcao == "3":
            # Consultar por Setor
            setor_consulta = input("Digite o setor a ser consultado: ")
            encontrados = []
            for funcionario in lista_funcionarios:
                if funcionario['setor'].lower() == setor_consulta.lower():
                    encontrados.append(funcionario)
            
            if not encontrados:
                print("Nenhum funcionário encontrado neste setor.")
            else:
                print(f"\nFuncionários no setor {setor_consulta}:")
                for funcionario in encontrados:
                    print(f"ID: {funcionario['id']}, Nome: {funcionario['nome']}, Salário: R$ {funcionario['salario']}")
        
        elif opcao == "4":
            # Retornar ao menu anterior
            return
        
        else:
            print("Opção inválida. Tente novamente.")

# E. Função para remover funcionário
def remover_funcionario():
    while True:
        id_remover = int(input("Digite o ID do funcionário a ser removido: "))
        encontrado = False
        for funcionario in lista_funcionarios:
            if funcionario['id'] == id_remover:
                lista_funcionarios.remove(funcionario)
                print(f"Funcionário com ID {id_remover} removido.")
                encontrado = True
                break
        if not encontrado:
            print("ID inválido. Funcionário não encontrado.")
        else:
            break

# F. Menu principal
while True:
    print("\nMenu Principal:")
    print("1. Cadastrar Funcionário")
    print("2. Consultar Funcionário")
    print("3. Remover Funcionário")
    print("4. Encerrar Programa")
    
    opcao_principal = input("Escolha uma opção: ")
    
    if opcao_principal == "1":
        # Cadastrar Funcionário
        cadastrar_funcionario(id_global)
    
    elif opcao_principal == "2":
        # Consultar Funcionário
        consultar_funcionarios()
    
    elif opcao_principal == "3":
        # Remover Funcionário
        remover_funcionario()
    
    elif opcao_principal == "4":
        # Encerrar Programa
        print("Programa encerrado.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")

# G. Lista de dicionários (lista_funcionarios já é a lista de dicionários)
# H. Comentários relevantes no código

