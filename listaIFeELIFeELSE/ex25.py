digi = int(input("Digite 1 para soma:\nDigite 2 para subtracao:\nDigite 3 para multiplicacao:\nDigite 4 para divisa\nDigite a opcao desejada: "))

numero1 = float(input("Digite o priemrio numero:"))
numero2 = float(input("Digite o segundo numero: "))

if digi == 1:
    res = numero1 + numero2
    print(res)

if digi == 2:
    res = numero1 - numero2
    print(res)

if digi == 3:
    res = numero1 * numero2
    print(res)

if digi == 4:
    res = numero1 / numero2
    print(res)