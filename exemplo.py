print('Cadastro')

nome = input("nome")
idade = input("idade")
serie = input("Sua serie")

nota1 = input("1º")
nota2 = input("2º")
nota3 = input("3º")

final = float(nota1) + float(nota2) + float(nota3)
divisao = (final) / 3

if divisao >= 6:
    print("Aprovado")
else:
    print("Reprovado precisa tirar uma nota melhor")

print("sua nota dos tres bimaestres",divisao)