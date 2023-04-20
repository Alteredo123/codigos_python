lata = int(input("Quantas latas você quer comprar? "))
gar600 = int(input("Quantas garrafas de 600ml você quer comprar? "))
gar2L = int(input("Quantas garrafas de 2 litros você quer comprar? "))

ml = (lata * 350) + (gar600 * 600) + (gar2L * 2000)
litros = ml / 1000

print(f"O total de ml comprado é {ml}ml e em litros é {litros:.2f}L")