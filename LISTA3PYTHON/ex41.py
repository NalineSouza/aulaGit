r1 = float(input("Digite o valor do resistor 1: "))
r2 = float(input("Digite o valor do resistor 2: "))

while(r1 != 0) and (r2 != 0):
    r = (r1 * r2) / (r1 + r2)

    print(r)
    
    r1 = float(input("Digite o valor do resistor 1: "))
    r2 = float(input("Digite o valor do resistor 2: "))


    