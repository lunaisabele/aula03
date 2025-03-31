# codigo para receber o nome de dois times e dizer qual é o vencedor
time1 = input("Nome do primeiro time: ")
time2 = input("Nome do segundo time: ")
#numero de gols de cada time
goldotime1 = int(input( "digite o numero de gols do time 1: "))
goldotime2 = int(input( "digite o numero de gols do time 2: "))

if goldotime1>goldotime2:
    print(f"vencedor: {time1}")
elif goldotime2 < goldotime1:
    print(f"vencedor:{time2}")
else:
    print("empate")
