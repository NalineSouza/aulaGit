num1 = int(input("Digite o numero: "))
num2 = int(input("Digite o segundo numero: "))

menor = 0
maior = 0

somapares = 0
multiimpares = 1

if num1 <= num2:

    menor = num1
    maior = num2

else:
    menor = num2
    maior = num1

while menor <= maior:

    if menor % 2 == 0:
        somapares = somapares + menor

    if menor % 2 != 0:
        multiimpares = multiimpares * menor

    menor = menor + 1
    
print(f"{somapares}, {multiimpares}")


