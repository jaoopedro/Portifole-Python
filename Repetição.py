print("SEJA BEM VINDO AO JOGO!!")
pontos = 0

pergunta6 = input("Qual a resposta da número 6? ") # QUESTÃO 6


if pergunta6 == "b":
    print("Você acertou!!")
    pontos += 3
else:
    pergunta6 = input("Qual a resposta da número 6? ")
    if pergunta6 == "b":
        pontos += 2
    else:
        pergunta6 = input("Qual a resposta da número 6? ")
        if pergunta6 == "b":
            pontos += 1

pergunta7 = input("Qual a resposta da numero 7? ") # QUESTÃO 7

if pergunta7 == "d":
    print("Você acertou!!")
    pontos += 3
else:
    pergunta7 = input("Qual a resposta da número 7? ")
    if pergunta7 == "d":
        pontos += 2
    else:
        pergunta7 = input("Qual a resposta da número 7? ")
        if pergunta7 == "d":
            pontos += 1


pergunta8 = input("Qual a resposta da número 8? ") # QUESTÃO 8

if pergunta8 == "a":
    print("Você acertou!!")
    pontos += 3
else:
    pergunta8 = input("Qual a resposta da número 8? ")
    if pergunta8 =="a":
        pontos += 2
    else:
        pergunta8 = input("Qual a resposta da número 8? ")
        if pergunta8 == "a":
            pontos += 1

pergunta9 = input("Qual a resposta da número 9? ") # QUESTÃO 9

if pergunta9 == "a":
    print("Você acertou!!")
    pontos += 3
else:
    pergunta9 = input("Qual a resposta da número 9?" )
    if pergunta9 == "a":
        pontos += 2
    else:
        pergunta9 = input("Qual a resposta da número 9?")
        if pergunta9 == "a":
            pontos += 1

pergunta10 = input("Qual a resposta da número 10? ") # QUESTÃO 10

if pergunta10 == "d":
    print("Você acertou!!")
    pontos += 3
else:
    pergunta10 = input("Qual a resposta da número 10? ")
    if pergunta10 =="d":
        pontos += 2
    else:
        pergunta10 = input("Qual a resposta da número 10? ")
        if pergunta10 =="d":
            pontos += 1
