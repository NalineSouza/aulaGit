valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

if (valor1 < valor2 + valor3) or (valor2 < valor3 + valor1) or (valor3 < valor1 + valor2):
    if valor1 == valor2 == valor3:
        print("Seu triângulo é equilátero!!")

    elif (valor1 == valor2):
        print("Seu triangulo é isosceles!!")

    elif (valor2 == valor3):
        print("Seu triangulo é  isosceles!!")

    elif (valor3 == valor1):
        print("Seu triengulo é  isosceles!!")

    elif (valor1 != valor2 != valor3):
        print("Seu triangulo é escaleno!!")

    else:
        print("Numero invalido!!")

    


    
