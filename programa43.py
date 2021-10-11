# Construir um program que leia um numero e diga sua Raiz quadrada
import math

n = float(input("Digite um número: "))

rq = math.sqrt(n)

saida = 'A raiz quadrada {0} é {1}'
print(saida.format(n,rq))
print()
print("* FIM DE PROGRAMA *")