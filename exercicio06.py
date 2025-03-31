# codigo para receber o nome de dois times e dizer qual é o vencedor
time1 = input("Nome do primeiro time: ")
goldotime1 = int(input( "digite o numero de gols do time 1: "))
time2 = input("Nome do segundo time: ")
goldotime2 = int(input( "digite o numero de gols do time 2: "))


if goldotime1==goldotime2:
    print("empate")
elif goldotime2 > goldotime1:
    print(f"vencedor:{time1}")
else:
    print(f"vencedor: {time2}")

