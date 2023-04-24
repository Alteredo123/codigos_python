km = float(input("Digite o percurso em km: "))
print("Escolha um tipo de carro: 1, 2 ou 3")
tipo = input("Qual tipo de carro você ta usando? ")

if tipo == "1":
    print(f"Com esse tipo de carro, você vai precisar de {km * 8} litros de gasolina\n")
elif tipo == "2":
    print(f"Com esse tipo de carro, você vai precisar de  {km * 9} litros de gasolina\n")
elif tipo == "3":
    print(f"Com esse tipo de carro, você vai precisar de {km * 12} litros de gasolina\n")
