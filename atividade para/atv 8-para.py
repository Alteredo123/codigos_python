divisor = 0
for cont in range(1, 200):
    divisor = cont % 4 
    if divisor == 0:
        print(cont)