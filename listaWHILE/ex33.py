lista = []
cont = 1

while cont <= 10:
    num = int(input("Digite um numero: "))
    lista.append(num)

    cont = cont + 1

valor2 = int(input("Digite o numero a ser acrescentado na lista: "))

if (valor2 in lista):
    print("o valor ja esta na lista")



