palavra = input("digite: ")

print("sem espaços: ---", palavra.strip(),"---") # "---" so foi usado para provar que tira espaço

# -> Metodo lower() e upper()
print("palavra em letras minuscula",palavra.lower())
print("palavra em letras MAIUSCULAS",palavra.upper())


# -> Metodo replace() substitiu um caractere / trecho por outra dentro da string
# Sintaxe: variavel.replace()

print("trocando a por X",palavra.replace("a","x"))
#                  (quem vai ser substituido/ quem vai substitiuir)

# uso do replace para remover espaços no meio
print("sem espaço no meio",palavra.replace(" ",""))


# -> Metodo split() divide a string em substrings, ou seja, divide em palavras/ um divisor/ divide oq estiver no split
# Sintaxe:  variavel.split("caratere_dellimitador")

print("Texto dividido", palavra.split(" "))


