cont = 1
total = 0
Conta = 0
while cont <= 8:
    nome = input("Digite seu nome: ")
    diaria = int(input("Quantas dias vai passar no hotel? "))
    if diaria < 15:
        taxa = diaria * 4
    elif diaria == 15:
        taxa = diaria * 3.60
    else:
        taxa = diaria * 3
    total = total + taxa + (diaria * 50)
    conta = (diaria * 50) + taxa
   
    print(f"O valor a ser pagor pelo sr/sra {nome} é: {conta}")
    print(f"-="*20)
    cont += 1
print(f"O faturamento total do hotel é de {total}")
