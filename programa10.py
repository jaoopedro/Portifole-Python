salarioF = float(input("digite seu salario: "))
vendas = float(input("digite o valor de suas vendas: "))

comissao = vendas * 0.04 # ou * 4 / 100

salario = salarioF + comissao

print("Sua comissão é de: R$", comissao)
print("Seu salario com a comissão é: R$", salario)