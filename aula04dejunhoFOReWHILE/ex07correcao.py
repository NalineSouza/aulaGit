n= int(input("Digite um numero de inteiros positivos:  "))
cont = 0
numero = 1

print("Os", n, "primeiros numeros impares naturais são")
while cont < n:
    print(numero)
    numero += 2
    cont += 1