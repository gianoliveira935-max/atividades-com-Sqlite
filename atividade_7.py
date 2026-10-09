nome = input("Digite o nome do trabalhador: ")
valor_hora = float(input("digite o valor do salário por hora: "))
horas_trabalhadas = float(input("digite as horas trabalhadas no mes: "))

salario = valor_hora * horas_trabalhadas
print(f"O salário do trabalhador {nome} é: R$ {salario:.2f}")
