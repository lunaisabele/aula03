#calcular dois horarios que saia no padrao 12 horas
hora1 = int(input("digite a hora: "))
minutos1 = int(input("digite os minutos: "))
hora2 = int(input("digite a hora: "))
minutos2 = int(input("digite os minutos: "))
somahor = hora1+hora2
somaminuts = minutos1+minutos2

if somaminuts >= 60 :
    somahor = somahor + 1

if somahor>=18:
    somahor= somahor-12

if somaminuts >= 24:
    somaminuts=somaminuts - 60

    print(f"{somahor} {somaminuts}")
