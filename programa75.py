# Exercicio 4 do estudo dirigido de Arrays

num = []
msg1 = 'Digite o {0}º numero: '

msg2 = 'Posição {0} = {1}'

for i in range(5):
    num.append(input(msg1.format(i+1)))

for i in range(5):
    print(msg2.format(i,num[i]))