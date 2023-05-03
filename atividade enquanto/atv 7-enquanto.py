cont = 1
soma = 0
while cont <= 4:
    num = int(input("Digite um número: "))
    soma = num + soma
    cont = cont + 1
print(f"A média dos valores lidos é {soma / cont}")