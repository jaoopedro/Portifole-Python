# Para saber qual o caracterie de acordo com a posição a sintaxe é variavel[e um numero de acordo]
# para pegar um trecho inteiro Sintaxe variavel[posição inicial: posição final]
#                                              [   inclusiva     : exclusive  ]

# USO DO len(variavel) serve para da a quantidade de caracteres

# saber a letra sem saber a palavra que digitaram variavel[qtd - 1]

palavra = input("Digite uma palavra: ")



print("A primeira letra é:", palavra[0])
print("A segunda letra é:", palavra[1])
print("A terceira letra é:", palavra[2])
print("trecho  entre a posição 2 é 8", palavra[2:8])

qtd = len(palavra)
#print("A palavra", palavra, "tem", qtd,"caracteres")
print("A ultima é",palavra[qtd - 1])



