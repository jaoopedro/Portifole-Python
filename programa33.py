# Exercicio 8 do estudo dirigido (estrutura de seleção if e else )

idade = int(input("Digite a idade: "))

if idade >=18:
    print("maior de idade")
    print("Maior em idade há",idade - 18,"anos")
else:
    print("menor de idade")
    print("Faltam",18 - idade ,"para ser maior")

print("* FIM DE PROGRAMA *")