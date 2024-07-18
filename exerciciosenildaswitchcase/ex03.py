print("A- Bife acebolado R$15")
print("B- Lasanha R$25")
print("C- Escondidinho R$18")
print("D- Ravioli R$30")
print("E- Macarronada R$25")
print("F- Carne Assada R$40")
print("G- Bife a Parmegiana R$30")
print("H- Frango a passarinho R$35")
print("I- Frango a parmegiana R$28")
print("J- Bife a Cavalo R$40")

menu = input("Escolha sua opção: ")

aceitataxa = input("Aceita pagar a taxa da garçom, SIM ou NAO: ")

gorjeta = 0.10


if menu == "A":
    valor = 15

if aceitataxa == "SIM":
    valor = (valor * 0.10) + valor
    print(f"O valor da sua conta ficou {valor}. ")

elif menu == "B":
    valor = 25

elif aceitataxa == "SIM":
    valor = (valor * 0.10) + valor
    print(f"O valor da sua conta ficou {valor}. ")

