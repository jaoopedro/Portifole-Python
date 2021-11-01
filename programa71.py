# exercício 16 do estudo dirigido sobre estrutura de repetição while

soma = 0
resposta = 'S'
qtd = 0
while resposta.upper() == 'S':

    nota = float(input('Digite a nota: '))


    while nota < 0 or nota > 10:

        print('NOTA INVALIDA!!!')
        preco = float(input('Digite NOVAMENTE o preço: R$ '))

    soma += nota
    qtd += 1

    resposta = input('Deseja continuar? <S/N>: ')

    while resposta.upper()!="S" and resposta.upper() != "N":
        print("RESPOSTA INVALIDA")
        resposta = input('Deseja continuar? <S/N>: ')

print('A soma das notas é', round(soma/qtd, 2))