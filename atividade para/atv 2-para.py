maior = 0
for contador in range(1,6):
    idade = int(input("Diga sua idade: "))
    if idade >= 18:
     maior = maior + 1
print(f"{maior} pessoas maior de idade")
    