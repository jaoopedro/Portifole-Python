from datetime import date
print('Data de hoje',date.today())
print()
data = int(input("Digite o ano do seu nascimento: "))
sexo = input("<M/F>: ")

idade = date.today().year - data

if idade == 18 and sexo.upper() =='M':
    print("Serviço militar Obrigatorio!!")
else:
    print("Insento do Serviço Militar!")