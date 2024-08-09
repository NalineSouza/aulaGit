produto = int(input("Digite o codigo do produto: "))

quantidade = int(input("Digite a quantidade do produto: "))

if produto == 100:
    res = quantidade * 12
    print(f"Seu hot-dog vai custar {res}.")

elif produto == 102:
    res = quantidade * 18.50
    print(f"Seu X-Salada vai custar {res}.")

elif produto == 103:
    res = quantidade * 25.50
    print(f"Seu X-Bacon vai custar {res}. ")

elif produto == 104:
    res = quantidade * 17
    print(f"Seu X-Burger vai custar {res}. ")

elif produto == 105:
    res = quantidade * 9.50
    print(f"Seu Suco de laranja vai custar {res}. ")

elif produto == 106:
    res = quantidade * 6
    print(f"Seu refrigerante vai custar {res}.")

else:
    print("Escolha um código de um produto  válido!!")