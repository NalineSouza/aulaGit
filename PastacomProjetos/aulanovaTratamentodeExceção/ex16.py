
try:
    numero_positivo_impar = int(input("Digite um numero:  "))
    contador = 1

    while(contador <= numero_positivo_impar):
        try:
            if(contador % 2 != 0):
                print(contador)

            contador = contador + 1
        except:
            print("Numero invalido!! digite outro!!!!")


except:
    print("Numero inválido!! digite outro!!")