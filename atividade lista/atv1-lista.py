
num = []
impar = 0
par = 0

for cont in range(1,11):
    num.append(cont)
    if cont % 2 == 0:
        par = par + 1    
    elif cont % 2 != 0:
        impar = impar + 1
print(f"A quantidades de números ímpares são : {impar}")
print(f"A quantidades de números pares são : {par}")

