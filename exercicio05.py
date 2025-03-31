# codigo para receber tres notas de um aluno e dizer se ele esta aprovado ou reprovado
nota1 = int(input("Dgite a sua nota: "))
nota2 = int(input("Dgite a sua nota: "))
nota3 = int(input("Dgite a sua nota: "))
# calculo da media do aluno
media = nota1 + nota2 + nota3/2

if media >= 7.0:
    print("aprovado\nparabens!")
else:
    print("reprovado!")
