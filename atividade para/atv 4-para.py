var1 = int(input("Digite um valor: "))
var2 = int(input("Digite outro valor: "))

soma = 0 

for cont in range(var1, var2 + 1):
    soma = soma + cont
print(soma)