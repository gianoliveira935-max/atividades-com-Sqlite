base_do_retangulo = float(input("Digite a base do retângulo: "))
altura_do_retangulo = float (input("Digite a altura do retângulo: "))

area_do_retangulo = base_do_retangulo * altura_do_retangulo

print(f"A área do retangulo é : {area_do_retangulo} metros quadrados")

perimetro_do_retangulo = 2 * (base_do_retangulo + altura_do_retangulo)
print(f"O perímetro do retangulo é : {perimetro_do_retangulo} metros")


diagonal_do_retangulo = (base_do_retangulo ** 2 + altura_do_retangulo ** 2) ** 0.5
print(f"A diagonal do retangulo é : {diagonal_do_retangulo} metros")

