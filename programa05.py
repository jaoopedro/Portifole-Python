# n1 = int(input("Digite um numero: "))
# n2 = int(input("Digite outro numero: "))

#               ou

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))


soma = (n1) + (n2)

subitracao = (n1) - (n2)

multiplicacao = (n1) * (n2)

potenciacao = (n1) ** (n2)

divreal = (n1) / (n2)

divint = (n1) // (n2)

resto = n1 % n2

print("A soma é", soma)
print("A subitracao é", subitracao)
print("A multiplicacao é", multiplicacao)
print("A potenciacao é", potenciacao)
print("A divisao real é", round(divreal, 2))
print("A divisao inteira é", divint)
print("o resto da divisao é", resto)