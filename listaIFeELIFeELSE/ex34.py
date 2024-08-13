precoantigo = float(input("Digite o preço antigo: "))

if (precoantigo < 50):
    taxa = precoantigo * 0.05
    res = taxa + precoantigo
    print(f"De acordo com a segunda tabela o preço atual desse produto é {res}")

elif (precoantigo >= 50) and (precoantigo <= 100):
    taxa = precoantigo * 0.10
    res = taxa + precoantigo
    print(f"De acordo com a segunda tabela o preço atual desse produto é {res}")

elif (precoantigo > 100):
    taxa = precoantigo * 0.15
    res = taxa + precoantigo
    print(f"De acordo com a segunda tabela o preço atual desse produto é {res}")