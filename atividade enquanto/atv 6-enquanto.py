import os #Importando biblioteca para trabalhar com sistema operacional 
cont = 1 
entre = 0
naoEntre = 0 

os.system("cls")#para limpar tela antes de executar o código o nome abaixo

while cont <= 5:
    num = int(input(f"Digite o {cont}°: "))
    if num >= 10 and num <= 20:
        entre += 1
    else:
        naoEntre += 1
    cont += 1

os.system("cls")

print(f"Tem {entre} números entre 10 e 20 \n")
print(f"Tem {naoEntre} que não estão entre 10 e 20 \n")