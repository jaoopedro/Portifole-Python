# Exercicio 5 do estudo dirigido de Arrays

num = []
msg1 = 'Digite o {0}º numero: '

for i in range(10):
    num.append(input(msg1.format(i+1)))

for i in range(9,-1,-1):
    print(num[i])