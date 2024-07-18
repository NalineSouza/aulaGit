valor = int(input("DIGITE UM NUMERO: "))
cont = 1

while valor % 2 == 0:
    print("O NUMERO DIGITADO NAO É IMPAR!!")
    valor = int(input("DIGITE UM NUMERO: "))

while cont <= valor:
    if cont % 2 != 0:
        print(cont)

    cont = cont + 1