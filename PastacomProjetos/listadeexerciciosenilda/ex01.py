num1 = float(input("Digite um numero: "))
num2 = float(input("Digite o segundo numero: "))


print("A- Adição")
print("S- Subitração")
print("M- Multiplicação")
print("D- Divisão")

res = input("Digite uma das opçoes para o tipo de operação que deseja: ")
 
if res == "A":
    resultado = num1 + num2
    print(f"O resultado da sua operação é {resultado}.")

elif res == "S":
    resultado = num1 - num2
    print(f"O resultado da sua operação é {resultado}.")

elif res == "M":
    resultado = num1 * num2
    print(f"O resultado da sua operação é {resultado}.")

elif res == "D":
    resultado = num1 / num2
    print(f"O resultado da sua operação é {resultado}.")