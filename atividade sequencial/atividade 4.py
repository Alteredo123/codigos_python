lata = int(input("Quantas latas você quer comprar? "))
gar600 = int(input("Quantas garrafas de 600ml você quer comprar? "))
gar2L = int(input("Quantas garrafas de 2 litros você quer comprar? "))

total = (lata * 350) + (gar600 * 600) + (gar2L * 2000) 
total1 = total / 1000

print(f"O total de ml comprado é {total}ml e em litros é {total1:.2f}L")