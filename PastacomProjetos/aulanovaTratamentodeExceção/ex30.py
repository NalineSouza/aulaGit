lista = []

while True:
    try:
        num = int(input("Digite um numero: "))
        
        if(num <= 0):
                break

        else:
            lista.append(num)

    except:
        print("Digite uma idade valida!!")


print(min(lista))
print(max(lista))