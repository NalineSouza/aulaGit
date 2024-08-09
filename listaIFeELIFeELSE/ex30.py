valor = float(input("Digite o valor do produto: "))

estado = input("Digite o estado desejado: ")

if estado == "MG":
    taxa = valor * 0.07
    res = taxa + valor
    print(f"O valor do produto é {res}: ")

elif estado == "SP":
    taxa = valor * 0.12
    res = taxa + valor
    print(f"O valor do produto é {res}: ")

elif estado == "RJ":
    taxa = valor * 0.15
    res = taxa + valor
    print(f"O valor do produto é {res}: ")

elif estado == "MS":
    taxa = valor * 0.08
    res = taxa + valor
    print(f"O valor do produto é {res}: ")

else:
    print("Seu estado não é válido!!")


