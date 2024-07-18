numero = int(input("Digite um numero inteiro maior do que zero: "))
if numero > 0:
    soma = 0
    numero__string = str(numero)

for i in numero__string:
    soma = soma + int(i)
    print(f"A soma dos algarismos de {numero} é {soma}.")

else:
    print("Por favor, digite um numero maior que zero.")
