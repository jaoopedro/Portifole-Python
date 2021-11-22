# Exercicio 5 do estudo dirigido de Funçoes

import math

def calcularComprimeto(R):
    C = 2 * math.pi * R
    print('O comprometo é',round(C,2))

def calcularArea(R):
    A = math.pi * (R **2 )
    print('A area é',round(A,2))

def calcularVolume(R):
    V = 3/4 * math.pi * (R**3)
    print('O volume é',round(V,2))

print('***** INÍCIO DO PROGRAMA *****')

raio = float(input('Digite o valor: '))

print('As operações são:')

print('(C) Comprimento')

print('(A) Área')

print('(V) Volume')


opcao = input('Digite a opção: ')

if opcao.upper() =='C':

    print('Comprimento da Esfera ')
    calcularComprimeto(raio)

elif opcao.upper() == 'A':

    print('Área da Esfera')
    calcularArea(raio)

elif opcao.upper() == 'V':

    print('Volume da Esfera')
    calcularVolume(raio)

else:
    print('OPÇÃO INVÁLIDA')

print('***** FIM DO PROGRAMA *****')
