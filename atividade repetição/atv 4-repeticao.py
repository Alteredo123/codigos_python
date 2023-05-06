cont = 1
otimo = 0
maiorIdade = 0
somaRuim = 0
mediaRuim = 0
maior = 0
print("A = Ótimo\nB = Bom\nC = Regular\nD = Ruim\nE = Péssimo") 
while cont <= 3:
    idade = int(input("Digite sua idade: "))
    
    while True:
        opniao = input("Diga sua opnião sobre o filme Vingadores guerra ifinita: ")
        if opniao == "a" or opniao == "b" or opniao == "c" or opniao == "d" or opniao == "e":
            break

    if opniao == "a":
        otimo += 1
    elif opniao == "d":
        somaRuim += idade

    if opniao == "a" and idade >= maiorIdade:
        maiorIdade = idade
    elif opniao == "d" and idade >= mediaRuim:
        maior = idade
    cont += 1
print("-=" * 20)
print(f"A quantidade de respostas ótimo foi: {otimo}\n")

print(f"A média de idade das pessoas que respoderam ruim foi: {somaRuim}\n")
if maiorIdade >= maior:
    print(f"A diferença de idade entre a maior idade que respondeu ótimo e a maior idade que respondeu ruim é {maiorIdade - maior}\n")
else:
    print(f"A diferença de idade entre a maior idade que respondeu ótimo e a maior idade que respondeu ruim é {maior - maiorIdade}\n")