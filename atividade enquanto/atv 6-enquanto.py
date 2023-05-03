cont = 1 
entre = 0
naoEntre = 0
while cont <= 5:
    num = int(input("Digite um número: "))
    if num >= 10 and num <= 20:
        entre = entre + 1
    elif num < 10 or num > 20:
        naoEntre = naoEntre + 1
    cont = cont + 1
print(f"Tem {entre} números entre 10 e 20 \n")
print(f"Tem {naoEntre} que não estão entre 10 e 20 \n")