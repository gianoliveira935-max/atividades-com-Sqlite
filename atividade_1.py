largura = float(input("Digite a largura do terreno: "))
altura = float(input("Digite a altura do terreno: "))
metros_quadrados = largura * altura
print(f"A área do terreno é: {metros_quadrados} metros quadrados")
preco_do_terreno = float(input("Digite o preço do terreno por metro quadrado: "))
valor_total = metros_quadrados * preco_do_terreno
print(f"O valor total do terreno é: R$ {valor_total:.2f}")
