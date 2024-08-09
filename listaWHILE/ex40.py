saida_a = float(input("Digite o valor inicial: "))
saida_b = float(input("Digite o valor final: "))
somaimpar = 0

if(saida_a > saida_b):
    print("Intervalo de valores invalido!!")


else:
    while(saida_a <= saida_b):
        if(saida_a % 2 != 0):
            somaimpar = somaimpar + saida_a
        saida_a = saida_a + 1

print(somaimpar)
        
