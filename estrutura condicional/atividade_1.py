aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

nota_final = nota1 + nota2
if nota_final >= 60:
    print(f"{aluno} foi aprovado com a nota {nota_final}")
else:
    print(f"{aluno} foi reprovado com a nota {nota_final}")