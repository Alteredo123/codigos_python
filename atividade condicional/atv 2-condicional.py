salario = float(input("Digite seu salário: "))

if salario < 600:
    salarioNovo = salario + (salario * (30/100))
    print(f" Seu novo salario é {salarioNovo}R$ \n")
else:
    print("Você não tem direito ao reajuste salarial \n") 