while True:
    num = int(input("Digite um número de 1 a 9: "))
    if num >= 1 and num <= 9:
        break
cont = 1
while cont <= 10:
    if num % 2 == 0:
        mult = cont * num 
        print(f"{num} x {cont} = {mult}")
    
    else:
        soma = cont + num
        print(f"{num} + {cont} = {soma}")
    cont = cont + 1