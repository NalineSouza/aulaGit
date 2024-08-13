def pot(x,y):
    res = x ** y
    return res

def verifica_idade(idade):
    if idade <= 0:
        return "Ta maluco!!"
    elif idade > 0 and idade < 99:
        return True
    else:
        "ta maluco, voce é muito velho"
    

def soma(n1,n2):
    res = n1 + n2
    return res

def mult(n1,n2):
    res = n1 * n2
    return res

print("CALCULAR POTENCIA!!!")
base = int(input)("Digite a base: ")
exp = int(input("Digit o expoente: "))

pot(base,exp)

x = pot(base,exp)
print(x)