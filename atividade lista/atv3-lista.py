valor = []

for contador in range (1,6) :
    valor.append(int(input(f"{contador} - Informe um valor :")))
valor.sort(reverse=True)
print (valor)