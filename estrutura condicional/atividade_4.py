operadora = ("vivo")
valor_plano_basico_em_minutos = 100
tempo = int(input("Digite o tempo de uso do plano em minutos: "))

if tempo <= valor_plano_basico_em_minutos:
    print("O valor do plano é: R$ 50,00")
else:
    valor_adicional = (tempo - valor_plano_basico_em_minutos) * 2
    print(f"O valor do plano é: R$ {50 + valor_adicional:.2f}")
