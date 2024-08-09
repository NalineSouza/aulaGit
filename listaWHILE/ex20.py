num = int(input("Digite um numero: "))
lidos = 0 #lidos
pares = 0
while num != 0:
    lidos += 1
    if num % 2 != 1:
        print(f"{num} é par!!!")
        pares += 1

    else:
        print(f"{num} Não é par!!!")
        num = int(input("Digite outro numero: "))

print("TOTAL DE NUMEROS LIDOS", lidos)
print("TOTAL DE PARES", pares)