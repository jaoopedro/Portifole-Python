# exercicio 12 do estudo dirigido (estrutura de seleção if e else )
# datetime biblioteca que atualiza a data em tempo real
from datetime import date

print("hoje é", date.today())
print()
ano = int(input("Digite o ano de nascimento: "))

idade = date.today().year - ano

print("sua idade é", idade)

if idade >= 16:
    print("Aptor a ser eleitor")
else:
    print("Inapt a ser eleitor")