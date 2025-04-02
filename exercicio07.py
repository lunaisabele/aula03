#codigo para ler o numero de litros vendidos e o tipo de combustivel utilizado
tipodecombustivel = input("digite qual tipo de combustivel voce quer: " )
litros = float(input("digete a quantidade de litros: "))
vgas = 5.8
veta = 4.9

if tipodecombustivel == "G":
    calculodagasolina = litros * vgas
    print(f"voce abasteceu {litros} "
          f"e gastou {calculodagasolina}" )
elif tipodecombustivel == "E" :
    calculodoetanol = litros * veta
    print(f"voce abasteceu {litros}" 
      f"e gastou {calculodoetanol}" )
else:
    print("solicitacao invalida" )









