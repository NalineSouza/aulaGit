distancia = float(input("Digite sua distancia: "))

litros = float(input("digite a quantidade de litros consumidos: "))

consumo = distancia / litros

if consumo < 8: 
    print("Venda o carro!!")

elif (consumo >= 8) and ( consumo <= 12):
    print("Economico!!")

else:
    print("Super economico!!")