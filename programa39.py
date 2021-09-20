# exercicio 16 do estudo dirigido (estrutura de seleção if e else )

n1 = float(input("Digite sua nota na AV1: "))
n2 = float(input("Digite sua nota na AV2: "))

media = (n1 + n2) /2
print("A media é",round(media,2))

if media >= 7:
    print(media,"Aprovado")
    print("* MEUS PARABÉNS * ")
else:
    n3 = float(input("Digite a nota de avaliação suplementar: "))

    media = (n1 + n2 + n3 *2)/4
    print("A nova media é", round(media,2))

    if media >=6:
        print("Aprovado")
    else:
        print("Reprovado")