# exercicio 12 estudo dirigido de while

soma = 0
msg='Digite a nota do aluno {0}: '

for i in range(1,11):
    nota = float(input(msg.format(i)))

    while nota <0 or nota >10:
        print("NOTA INVALIDA")
        nota = float(input(msg.format(i)))

    soma+=nota
print("A media da turma é",round(soma/i, 2))