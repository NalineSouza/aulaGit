print("A- Bife acebolado R$15")
print("B- Lasanha R$25")
print("C- Escondidinho R$18")
print("D- Ravioli R$30")
print("E- Macarronada R$25")


menu = input("Escolha sua opção: ")

aceitataxa = input("Aceita pagar a taxa da garçom, SIM ou NAO: ")



if menu == "A":
    valor = 15

if aceitataxa == "SIM":
    valor = (valor * 0.10) + valor
    print(f"O valor da sua conta ficou {valor}. ")
    

if aceitataxa == "NAO":
    print(f"O valor da sua conta é {valor}")

if menu == "B":
    valor = 25

if aceitataxa == "SIM":
    valor = 25
    valor = (valor * 0.10) + valor
    print(f"O valor da sua conta ficou {valor}. ")

