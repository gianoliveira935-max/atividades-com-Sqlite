pessoa_1 = input("Digite o nome da primeira pessoa: ")
idade_pessoa_1 = int(input("Digite a idade da primeira pessoa: "))

pessoa_2 = input("Digite o nome da segunda pessoa: ")
idade_pessoa_2 = int(input("Digite a idade da segunda pessoa: "))

media = (idade_pessoa_1 + idade_pessoa_2) / 2
print(f"A média das idades de {pessoa_1} e {pessoa_2} é: {media:.2f} anos")

