# Programa 81 mais completo.

def calcularMedia():

    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))
    print('A media é', (n1 + n2)/2)

def calcularDifereca():
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))

    if n1 > n2:
        print('A diferença é',n1 - n2)
    else:
        print('A diferença é',n2 - n1)

def calcularProduto():

    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))
    print('O Produto é', n1*n2)

def calcularDivisao():

    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))
    print('A divisão é',n1/n2)

def exibirOpcoes():

    print('As operações são:')

    print('(1) Média Aritmética')

    print('(2) Diferença do maior pelo menor')

    print('(3) Produto')

    print('(4) Divisão')

    opcao = int(input('Digite a opção: '))

    if opcao ==1:
        print('Media Aritmetrica')
        calcularMedia()
    elif opcao ==2:
        print('Diferença')
        calcularDifereca()
    elif opcao ==3:
        print('Produto')
        calcularProduto()
    elif opcao ==4:
        print('Divisão')
        calcularDivisao()
    else:
        print('OPÇÃO INVALIDA!!!')
        exibirOpcoes()

print('***** INÍCIO DO PROGRAMA *****')

exibirOpcoes()

print('***** FIM DO PROGRAMA *****')