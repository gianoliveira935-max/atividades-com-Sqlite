medida_a = float(input("Digite a medida A: "))
medida_b = float(input("Digite a medida B: "))
medida_c = float(input("digite a medida c: "))

area_do_quadrado = medida_a ** 2    
print(f"A área do quadrado é: {area_do_quadrado:.4f}")

area_do_triangulo = (medida_a * medida_b) / 2
print(f"A área do triangulo é: {area_do_triangulo:.4f}")

area_do_trapezio = ((medida_a + medida_b) * medida_c) / 2
print(f"A área do trapezio é: {area_do_trapezio:.4f}")



