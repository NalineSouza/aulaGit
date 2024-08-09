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


print(f"O menor numero digitado foi"(min(lista)))
print(f"O maior numero digitado foi"(max(lista)))
