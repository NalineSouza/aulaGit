valor = int(input("DIGITE UM NUMERO: "))
cont = 0

while valor % 2 != 0:
    print("NUMERO DIGITADO NAO É PAR!!")
    valor = int(input("DIGITE UM NUMERO: "))

while cont <= valor:
    if cont % 2 == 0:
        print(valor)
    valor =  valor - 1