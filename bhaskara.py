import math

b = int(input("Entre com o valor de B"))
a = int(input("Entre com o valor de A"))
c = int(input("Entre com o valor de C"))

delta = (b**2) - 4*a*c
raiz = math.sqrt(delta)

x_1 = (- b - raiz)/(2*a)
x_2 = (- b + raiz)/(2*a)

print(x_1 , x_2)

if x_1 >0:
    print('Este é o valor correto',x_1)
if x_2 > 0:
    print('Utilize este valor',x_2)

