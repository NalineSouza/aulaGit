turno = input("Digite a primeira letra do turno que voce estuda: ")

if (turno == "M") or (turno == "m"):
    print("Voce estuda no turno da manha, BOM DIA!")

elif(turno == "V") or (turno == "v"):
    print("Voce estuda no turno da tarde, BOA TARDE!")

elif(turno == "N") or (turno == "n"):
    print("Voce estuda no turno da noite, BOA NOITE!")

else:
    print("Turno invalido!!!!")