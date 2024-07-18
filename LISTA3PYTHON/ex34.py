listanumero = []
listapar = []
listaimpar = []
cont = 0

while cont < 20:
    num = int(input("Digite o numero: "))
    listanumero.append(num)
    
    if(num % 2 == 0):
        listapar.append(num)

    else:
        listaimpar.append(num)

    cont = cont + 1

print(listanumero)
print(listapar)
print(listaimpar)


