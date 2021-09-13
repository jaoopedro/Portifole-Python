# Exercicio 4 do estudo dirigido (estrutura de seleção if e else )

nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
nota3 = float(input("Digite sua nota: "))

media = (nota1 + nota2 + nota3) / 3
if media >= 6:
    print("Aprovado",round(media,2))
    print("Passou com",round(media - 6,2) )


print("*FIM DE PROGRAMA*")