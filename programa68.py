# exercicio 10 estudo dirigido de while

soma = 0
msg='Digite o preço do produto{0}: R$ '

for i in range(1,11):
    preco= float(input(msg.format(i)))

    while preco <=0:
        print('PREÇO INVALIDO')
        preco = float(input(msg.format(i)))

    soma += preco

print('A soma dos preços é R$',round(soma,2))