palavra = input("digite: ")

print("sem espaços: ---", palavra.strip(),"---") # "---" so foi usado para provar que tira espaço

# Metodo lower() e upper()
print("palavra em letras minuscula",palavra.lower())
print("palavra em letras MAIUSCULAS",palavra.upper())

# Metodo replace() substitiu um caractere / trecho por outra dentro da string
# Sintaxe variavel.replace()

print("trocando a por X",palavra.replace("a","x"))
#                  (quem vai ser substituido/ quem vai substitiuir)
