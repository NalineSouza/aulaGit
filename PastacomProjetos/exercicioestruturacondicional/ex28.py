num1 = int(input("Digite um numero: "))
num2 = int(input("Digite o segundo numero: "))

print(" A- Para ADIÇÃO: ")
print(" B- Para SUBITRAÇÃO: ")
print(" C- Para MULTIPLICAÇÃO: ")
print(" D- Para DIVISÃO: ")
opcao = input("Escolha uma opção de conta: ")

if opcao == "A":

    var1 = num1 + num2
    print(var1)
    

if opcao == "B":
    var2 = num1 - num2
    print(var2)


elif opcao == "C":
    var3 = num1 * num2
    print(var3)


elif opcao == "D":
    var4 = num1 / num2
    print(var4)

elif (opcao != "A"  ) or (opcao != "b" ) or (opcao != "C" ) or (opcao != "D"):
    print("Opção Inválida!!")





