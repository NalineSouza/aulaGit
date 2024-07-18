num = int(input("Digite um numero entre 100 e 9999: "))

while (num < 100) or (num > 9999):
    print("ÍNVALIDO")
    num = int(input("Digite um numero entre 100 e 9999: "))


numerostring = str(num)

for algarismo in numerostring:
    print(algarismo)