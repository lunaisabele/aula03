# codigo para ler o nome de uma pessoa sua idade e seu salario e mostrar no final
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salario: "))
# usuario digita o seu aumento, tem o seu percentual calculado
aumento = float(input("Digite o seu percentual de aumento: "))
percentual = salario*aumento/100
# soma do salario com o aumento, mostrando o resultado no final
salario_final = salario+percentual
print(f"o percentual de aumento foi de: {percentual}\n ")
print(f"seu nome: {nome}\nsua idade: {idade}\nseu salario: {salario}\n"
      f"salario com aumento: {salario_final} ")
