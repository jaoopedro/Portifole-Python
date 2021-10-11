# Construir um program que leia um numero e diga sua Raiz quadrada
import math

n = float(input("Digite um número: "))


if not(n < 0): #quando o not for falso ele executa
    rq = math.sqrt(n)
    saida = 'A raiz quadrada {0} é {1}'
    print(saida.format(n,round(rq, 2)))
else:
    print("nao existe raiz quadrada de numeros negativos no conjuto de numeros reais")