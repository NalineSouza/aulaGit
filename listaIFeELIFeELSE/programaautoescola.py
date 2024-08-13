#Programa auto escola RapiCNH

idade = int(input("digite sua idade:"))
teste_psicotecnico = "APROVADO"
prova_teórica = 7.0

if(idade >= 18):
    print("Tem idade para tirar CNH")
    if(teste_psicotecnico == "APROVADO" and prova_teórica >= 7.0):
       print("Está apto para fazer as aulas práticas!")
    elif(teste_psicotecnico == "REPROVADO" or prova_teórica < 7.0):
       print("Não está apto para fazer as aulas práticas!")
else:
   print("Não tem idade para tirar CNH")