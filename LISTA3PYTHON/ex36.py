mediasporaluno = []
contaluno = 0
contanota = 0
media = 0

while(contaluno < 10):
    print(f"Aluno{contaluno}")
    while(contanota < 4):
        nota = float(input(f"Digite a nota {contanota}: "))
        media = media + nota
        contanota = contanota + 1
    
    media = media / 4
    mediasporaluno.append(media)
    media = 0

    contanota = 0
    contaluno = contaluno + 1

print(mediasporaluno)

    
