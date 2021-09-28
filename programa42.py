A = float(input("insira o valor de A: "))
B = float(input("insira o valor de B: "))
C = float(input("insira o valor de C: "))


if A >= B + C or B >= C + A or C >= B + A:
    print("Não Forma um triangulo")
else:
    print("Forma um triangulo")
    if A == B and B == C:
        print("triangulo equilatero")
    elif A == B and B != C:
        print("Triangulo isosceles")
    else:
        print("Triangulo escaleno")