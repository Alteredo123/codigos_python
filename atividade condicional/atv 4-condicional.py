sexo = input("Digite seu sexo: ")
altura = float(input("Digite sua altura: "))

if sexo == "m":
    calc = (72.7 * altura) - 58
    print(calc)
elif sexo == "f":
    calc = (62.1 * altura) - 44.7
    print(calc)