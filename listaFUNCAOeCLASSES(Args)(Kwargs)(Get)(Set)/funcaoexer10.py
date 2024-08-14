def Simular_Financiamento(valor_veiculo,valor_entrada,taxa_juros,quantidade_parcelas):
    valorveiculo = (valor_veiculo - valor_entrada) / quantidade_parcelas
    valorparcela = valorveiculo * taxa_juros

    return valorparcela


valorvei  = float(input("Digite o valor do veiculo:  "))
valorentr = float(input("Digite o valor da entrada:  "))
valorjuros = float(input("Digite o valor do juros:  "))
valorparce = int(input("Digite a quantidade de parcelas:  "))

resultado = Simular_Financiamento(valorvei,valorentr,valorjuros,valorparce)

print(resultado)
print(f"Sua entrada foi de {valorentr}")
print(f"O valor do veiculo é {valorvei}")
print(f"O valor do juros é {valorjuros}")
print(f"O valor total do veiculo com juros é {valorparce}")
