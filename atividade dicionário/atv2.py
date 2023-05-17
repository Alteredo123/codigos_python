
lista = list()
contato = dict()

for contador in range(0,7):
    nome = input("Informe o nome do individuo: ")
    contato[nome] = int(input(f"Informe o número de {nome}: "))

    lista.append(contato.copy())# copiar o conteúdo do dicionário para a lista   
    contato.clear()# limpar o conteúdo do dicionário
print(lista)