salario = float(input("Qual seu salário? "))
valorFinanciamento = float(input("Qual valor do financiamento? "))

valor = valorFinanciamento * 5 
if valor <= salario:
    print("Financiamento concedido!")
else:
    print("Financiamento negado!")

print("Obrigado por nos consultar!")