idade = int(input("Qual a sua idade : "))

def categoria(num):
    if num >=5 and num <= 7:
        return"INFANTIL A"
    if num >=8 and num <= 10:
        return"INFANTIL B"
    if num >=11 and num <=13:
        return"JUVENIL A"
    if num >=14 and num <=18:
        return"JUVENIL B"
    
print(categoria(idade))
    
    


