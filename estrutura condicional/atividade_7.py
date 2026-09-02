for i in range(3):
    distancia_dos_dardos_lançados = float(input("Digite a distância do dardo lançado: "))

maior_distancia = 0
for distancia in [distancia_dos_dardos_lançados]:
    if distancia > maior_distancia:
        maior_distancia = distancia

print(f"A maior distância é: {maior_distancia}")