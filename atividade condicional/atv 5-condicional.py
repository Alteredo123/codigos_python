km = float(input("Digite o percurso em km: "))
print("Escolha um tipo de carro: 1, 2 ou 3")
tipo = input("Qual tipo de carro você ta usando? ")

if tipo == "1":
    total = km / 8
    #print(f"Com esse tipo de carro, você vai precisar de {km / 8:.2f} litros de gasolina\n")
elif tipo == "2":
    total = km / 9
    #print(f"Com esse tipo de carro, você vai precisar de  {km / 9:.2f} litros de gasolina\n")
elif tipo == "3":
    total = km / 12
    #print(f"Com esse tipo de carro, você vai precisar de {km / 12:.2f} litros de gasolina\n")
else:
    total = 0
    print("Esse valor é inválido!")

print(f"Com o tipo de carro {tipo}, você vai precisar de {total:.2f} litros de gasolina\n")
