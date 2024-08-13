numAvaliacoes = int(input("Digite o numero de avaliações: "))

somaNotas = 0

for i in range(numAvaliacoes):
    #receber a nota
    nota = float(int("Digite a nota da avaliação {}:".format(i+1)))
    somaNotas += nota 

    media = somaNotas / numAvaliacoes

    print(media)