valor = int(input("Informe um valor qualquer: "))

maior = 0 
posicao = 0 

for cont in range(1, valor + 1):
    item = int(input("Informe um valor: "))
    if item >= maior:
        maior = item
        posicao = cont
print(f"O maior número está na posição {posicao}° e é {maior}")