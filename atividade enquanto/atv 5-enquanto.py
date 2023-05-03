num = int(input("Digite um número: "))
cont = 1
while cont <= 10:
    if num % 2 == 0:
        mult = cont * num 
        print(f"{cont} x {num} = {mult}")
    
    elif num % 2 == 1:
        soma = cont + num
        print(f"{cont} + {num} = {soma}")
    cont = cont + 1