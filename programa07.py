import math

r = float(input("digite o raio da esfera: "))

C = 2 * math.pi * (r)
A = math.pi * r ** 2
V = 3/4 * math.pi * (r ** 3)

print("o comprimento da esfera é: ", round(C, 2))
print("sua area é: ",round(A, 2))
print("sru volume é: ",round(V, 2))