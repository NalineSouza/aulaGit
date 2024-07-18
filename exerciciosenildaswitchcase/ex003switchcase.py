import math



 
print("1- Bife acebolado R$15")
print("2- Lasanha R$25")
print("3- Escondidinho R$18")
print("4- Ravioli R$30")
print("5- Macarronada R$25")
print("6- Carne Assada R$40")
print("7- Bife a Parmegiana R$30")
print("8- Frango a passarinho R$35")
print("9- Frango a parmegiana R$28")
print("10- Bife a Cavalo R$40")

menu = int(input("Digite a opção desejada: "))

match menu:

  case 1:
     valor = 15

  case 2:
     valor = 25

  case 3:
     valor = 18

  case 4:
     valor = 30

  case 5:
     valor = 25

  case 6:
     valor = 40

  case 7:
     valor = 30
 
  case 8:
     valor = 35

  case 9:
     valor = 28

  case 10:
     valor = 40


aceitataxa = input("Aceita a taxa de 10%, SIM/NAO: ")

match aceitataxa:
   case "SIM":
   
      valorfinal = valor + (valor * 0.10)
      print(F"O valor final a ser pago é {valorfinal} reais.")

   case "NAO":
      print(F"O valor da sua conta é {valor} reais.")
   case _:
     print("Opção Invalida!!")