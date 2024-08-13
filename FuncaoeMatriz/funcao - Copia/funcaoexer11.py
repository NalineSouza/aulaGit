frutas = ['pera', 'banana', 'goiaba', 'kiwi', 'arroz doce']

def imprima(lista):
    i = 0
    while i < len(lista):
        print(f"{i+1}, {lista[i]}")
        i += 1
imprima(frutas)

def imprima2(lista):
    cont = 1
    for item in lista:
        print(f"{cont}, {item}")
        cont += 1
imprima(frutas)