salario = float(input("Qual seu salário? "))
valorFinanciamento = float(input("Qual valor do financiamento? "))

if valorFinanciamento <= 5 * salario:
    print("Financiamento concedido!")
else:
    print("Financiamento negado!")