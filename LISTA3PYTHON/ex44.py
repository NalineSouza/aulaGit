num1 = float(input("Digite um numero: "))
num2 = float(input("Digite o segundo numero: "))

opcao = int(input("Para adição digite 1\n Para subtração digite 2\n Para multiplicação digite 3\n Para divisão digite 4\n Para sair digite 5:  "))

while(opcao != 5):
    if(opcao == 1):
        resultado = (num1 + num2)
        print(resultado)

    if(opcao == 2):
        resultado = (num1 - num2)
        print(resultado)

    if(opcao == 3):
        resultado = (num1 * num2)
        print(resultado)

    if(opcao == 4):
        resultado = (num1 / num2)
        print(resultado)

    if(opcao > 5):
        print("Opção invalida!!")


    opcao = int(input("Para adição digite 1/n Para subtração digite 2/n Para multiplicação digite 3/n Para divisão digite 4/n Para sair digite 5 "))



    