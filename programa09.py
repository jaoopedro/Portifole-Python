# pesoMais = pesoMenos = peso
#    <-        <-        <-

peso = float(input("digite seu peso: "))
pesoMais = pesoMenos = peso

peso15 = peso * 0.15
peso20 = peso * 0.20

pesoMais += peso15
pesoMenos -= peso20

print("O peso se engordar 15% é: ", pesoMais)
print("O peso se emagrecer 20%", pesoMenos)