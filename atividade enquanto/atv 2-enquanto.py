maior = 0
num = 1
"""while True:
    num = int(input("Insira um valor: "))
    if num >= maior:
        maior = num
    if num == 0:
        break
print(f"O maior valor foi {maior}")"""


while num != 0:
    num = int(input("Insira um valor: "))
    if num >= maior:
        maior = num
print(f"O maior valor foi {maior}")