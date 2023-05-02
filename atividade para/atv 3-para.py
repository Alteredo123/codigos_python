a = 0
cont = 0
x = int(input("Digite um número: "))
for cont in range(1, x + 1):
    a = x % cont 
    if a == 0:
        print(f"{cont} é divisor de {x}")