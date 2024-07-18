produto = float(input("Digite o valor do produto comprado: "))

if produto < 50:
    valor = (produto * 0.45) + produto
    print(f"O valor para revenda é {valor} reais")

else:
    valor = (produto * 0.30) + produto
    print(f"O produto esta no valor de {valor} reais")
