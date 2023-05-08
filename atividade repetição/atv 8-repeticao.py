soma = 0
for cont in range(85, 908):
    if cont % 2 == 0:
        soma = soma + cont
        print(cont)
print("*" * 20)

print(f"A soma dos valores par entre 85 e 907 é {soma}")
