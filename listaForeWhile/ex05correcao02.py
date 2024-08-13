palavra = input("Digite uma palavra: ")

print("Posição de cada letra")
for i, letra, in enumerate(palavra):
    print("Posição {}: {}".format(i,letra))

print("O programa foi finalizado") 