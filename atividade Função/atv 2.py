while True:
    a = int(input("Informe um valor qualquer: "))
    b = int(input("Informe um outro valor qualquer: "))

    if a != b:
        break

def somImpar(inicial,final):
    soma = 0
    for percorrer in range(inicial,final + 1):
        if percorrer % 2 == 1:
            soma += percorrer
    return soma

def mediaMultiplo3(inicial, final):
    total = 0
    contDivisores = 0
    for percorrer in range(inicial,final + 1):
        if percorrer % 3 == 0:
            total += percorrer # Isto é para somar todos os divisores
            contDivisores += 1 # Isto é para contar todos os divisores
    
    return total/contDivisores

if a < b:
    print(f"A soma dos impares é : {somImpar(a,b)}")
else:
    print(f"A média dos múltipos de 3 é: {mediaMultiplo3(b,a)}")
    


        
