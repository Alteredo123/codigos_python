"""num = int(input("Digite um número maior que zero: "))
cont = 1
while cont <= num:
    print(cont)
    cont = cont + 1"""
cont = 1
while True:
    num = int(input("Digite um número qualuqer: "))
    if num > 0:
        break

while cont <= num:
    print(cont)
    cont = cont + 1