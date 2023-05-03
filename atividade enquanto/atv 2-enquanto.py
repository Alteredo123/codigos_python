maior = 0
while True:
    num = int(input("Insira um valor: "))
    if num >= maior:
        maior = num
    if num == 0:
        break
print(f"O maior valor foi {maior}")