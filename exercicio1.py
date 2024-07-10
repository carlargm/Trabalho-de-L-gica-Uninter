print("Bem-vindos a loja da Carla Regina Gomes Moreira Do Carmo")
valorDoPedido = float(input("Digite o valor do pedido: "))
quantidadeParcelas = int(input("Digite a quantidade de parcelas: "))

if quantidadeParcelas < 4: 

    juros = 0 

elif quantidadeParcelas < 6: 

    juros = 0.04  # 4% 

elif quantidadeParcelas < 9: 

    juros = 0.08  # 8% 

elif quantidadeParcelas < 13: 

    juros = 0.16  # 16% 

else: 

    juros = 0.32  # 32% 

valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas

print("Programadora: Carla Moreira")

if quantidadeParcelas >= 4:
    print(f"Quantidade de parcelas: {quantidadeParcelas}")
    print(f"Valor da parcela: R${valorDaParcela:.2f}")
    print(f"Valor total parcelado: R${valorTotalParcelado:.2f}")
else:
    print("Para parcelamentos com menos de 4 parcelas, não há juros.")