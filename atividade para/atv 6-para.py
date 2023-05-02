somaIdade = 0
mediaIdade = 0 

somaPeso = 0
mediaPeso = 0
for cont in range(1,5 + 1):
    idade = int(input("Digite sua idade: "))
    Peso = float(input("Digite seu peso: "))
    print("*" * 30)

    somaIdade = somaIdade + idade
    mediaIdade = somaIdade / cont

    somaPeso = somaPeso + Peso
    mediaPeso = somaPeso / cont

print(f"O peso médio desse time é {mediaPeso}Kg")
print(f"A media das idades desse time é {mediaIdade}")