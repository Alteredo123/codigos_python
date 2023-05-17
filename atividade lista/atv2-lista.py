from random import randint
num = []
posi =0 

for cont in range (1,11) :
    num.append(randint(1,15))
    print ("-" * 30)
    if num[cont - 1] == 10:
        posi = cont
        print (f"{num[cont - 1]} é igual a 10, e esta na posição {cont}")

print(num)