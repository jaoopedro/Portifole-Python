# exercicio 6 do estudo dirigido sobre estrutura de repetição for

for i in range(1,4):
    print("*** Aluno",i,"***")
    n1=float(input("Digite a nota 1: "))
    n2 = float(input("Digite a nota 2: "))
    n3 = float(input("Digite a nota 3: "))
    media = (n1 +n2 + n3)/3
    print("A media é",round(media,2))
    if media >=6:
        print("Aluno Aprovado")
    else:
        print("Aluno Reprovado")