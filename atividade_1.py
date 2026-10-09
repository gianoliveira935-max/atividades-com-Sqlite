largura = float(input("Digite a largura do terreno: "))
altura = float(input("Digite a altura do terreno: "))

area_do_terreno = largura * altura
print(f"A área do terreno é: {area_do_terreno} metros quadrados")

preco_do_terreno = float(input("Digite o preço do terreno por metro quadrado: "))

valor_total = area_do_terreno * preco_do_terreno

print(f"O valor total do terreno é: R$ {valor_total:.2f}")
