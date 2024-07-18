valorvenda = float(input("Digite o valor da venda: "))

if (valorvenda >= 100000):
    comissao = (valorvenda * 0.16) + 700
    print(f"O valor da sua comissão é {comissao}")

elif (valorvenda < 100000) and (valorvenda >= 80000):
    comissao = (valorvenda * 0.14) + 650
    print(f"O valor da sua comissão é {comissao}")

elif (valorvenda < 80000) and (valorvenda >= 60000):
    comissao = (valorvenda * 0.14) + 600
    print(f"O valor da sua comissão é {comissao}")

elif (valorvenda < 60000) and ( valorvenda>= 40000):
    comissao = (valorvenda * 0.14) + 550
    print(f"O valor da sua comissão é {comissao}")

elif (valorvenda < 40000) and (valorvenda >= 20000):
    comissao = (valorvenda * 0.14) + 500
    print(f"O valor da sua comissão é {comissao}")

elif (valorvenda < 20000):
    comissao = (valorvenda * 0.14) + 400
    print(f"O valor da sua comissão é {comissao}")
