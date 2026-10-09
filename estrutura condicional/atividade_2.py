import math

a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Nao existem raizes reais")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    print(f"x1 = {x1:.4f}")
    print(f"x2 = {x2:.4f}")
