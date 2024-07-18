nota = float(input("Digite sua nota: "))
lista = []
media = 0
while (nota >= 0) and (nota <= 10):
    lista.append(nota)
    nota = float(input("Digite sua nota: "))

for valor in lista:
    media = media + valor


media = media / len(lista)

print(media)
