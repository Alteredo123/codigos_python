cont = 1
maior = 0
media = 0
mediaTurma = 0
mulher = 0
while cont <= 6:
    while True:
        sexo = int(input("Digite 1 para masculino e 2 para feminino: "))
        if sexo == 1 or sexo == 2:
            break
    altura = float(input("Digite sua altura: "))
    if altura > maior:
        maior = altura
    elif cont == 1:
        menor = altura
    else:
        menor = altura
        
    if sexo == 2:
        mulher += 1
        media += altura 

    mediaTurma += altura
    cont += 1
  

print(f"A maior altura da turma é de {maior:.2f}")
print(f"A menor altura da turma é de {menor:.2f}")
print(f" A média de altura das mulheres é de {media / mulher:.2f}")
print(f"A média de altura da turma é de {mediaTurma / cont:.2f}")