listaconso = []
listavogal = ["a", "e", "i", "o", "u", "A", "E", "I","O", "U"]
cont = 0

while cont < 10:
    letra = input("Digite uma letra: ")
    if letra not in listavogal:
        listaconso.append(letra)

    cont = cont + 1

print(f"Foram lidas {len(listaconso)} consoantes")
print(listaconso)