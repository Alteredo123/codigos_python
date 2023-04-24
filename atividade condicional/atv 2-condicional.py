salario = float(input("Digite seu salário: "))

if salario <= 600:
    salarioNovo = salario + (salario * (30/100))
    print(salarioNovo)
else:
    print("Você não tem direito ao reajuste salarial \n") 