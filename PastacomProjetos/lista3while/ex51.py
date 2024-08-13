brancos = 0
nulos = 0
ana = 0
bia = 0
cris = 0
duda = 0

while True:
    print("Eleições 2024")
    print("Favor escolha sua Candidata!!!")
    print("1 - ANA \n 2 - Bia \n 3 - Cris \n 4 - Duda")
    print("5 - Branco \n 6 - Nulo")
    voto = int(input("Digite seu voto: "))
    if voto == 0:
        break
    elif voto == 1: