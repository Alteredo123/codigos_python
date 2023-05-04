import os
cont = 1
soma = 0

os.system("cls")

while cont <= 4:
    num = int(input(f"Digite o {cont}° número: "))
    soma = num + soma
    cont = cont + 1
print(f"A média dos valores lidos é {soma / cont}")