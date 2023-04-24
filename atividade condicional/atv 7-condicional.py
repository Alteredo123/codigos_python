a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

if a < b + c and b < a + c and c < a + b:
    print("Os valores formam um triângulo.")
else:
    print("Os valores não formam um triângulo.")
