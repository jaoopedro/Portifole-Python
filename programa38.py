# exercicio 16 do estudo dirigido (estrutura de seleção if e else )

qtd = int(input("Digite a quantidade de dicipinas sem aprovação: "))

if qtd ==0:
    print("Aluno Aprovado")
elif qtd <=5:
    print("Aluno Recuperação")
else:
    print("Aluno Reprovado")

print()
print("* FIM DE PROGRAMA *")