numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

multiplos = numero1 % numero2 == 0 or numero2 % numero1 == 0
if multiplos:
    print(f"{numero1} e {numero2} são múltiplos")
else:
    print(f"{numero1} e {numero2} não são múltiplos")
