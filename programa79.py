# Exercicio 2 do estudo dirigido de Funçoes

def calcularQuadrado():
    n = int(input('Digite um numero: '))
    msg = 'O quadrado de {0} é {1}'
    print(msg.format(n,n ** 2))

print('*** INICIO DO PROGRAMA ***')

calcularQuadrado()

print('*** FIM DO PROGRAMA ***')