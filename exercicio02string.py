nome = input("seu nome: ")
cpf = input("Digite o cpf (somente numeros): ")

cpff = cpf[0:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:11]

print("seu cpf é", cpff)
