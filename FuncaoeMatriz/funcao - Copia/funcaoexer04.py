'''
Escreva um programa, com uma função que necessite de um
argumento. A função retorna o valor de caractere 'P', se seu argumento for 
positivo, e 'N', se seu argumento for zero ou negativo.

'''

def positivo_negativo(n1):
    if n1 > 0:
        print("P")

    else:
        print('N')


positivo_negativo(-8)
positivo_negativo(10)
positivo_negativo(0)