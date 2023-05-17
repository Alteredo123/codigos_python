lista = list()
valor = dict()

for cont in range(0,1):
    nome = input("Informe o nome do prato: ")
    valor[nome]= (input(f"Informe o valor do prato {nome}: "))

lista.append(valor.copy())
valor.clear()

print(lista)