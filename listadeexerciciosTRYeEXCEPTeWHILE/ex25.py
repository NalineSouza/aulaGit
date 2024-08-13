
listaidade = []

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if(idade <= 0):
            break

        else:
            listaidade.append(idade)
    except:
        print("Idade invalida!! digite novamente!!")

print(sum(listaidade) / len(listaidade))
