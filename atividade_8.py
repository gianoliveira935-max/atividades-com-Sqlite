kms_percorridos = float(input("digite a quantidade de kms percorridas:"))
combustivel_gasto = float(input("digite a quantidade de combustivel gasto na viagem: "))

consumo_medio = kms_percorridos / combustivel_gasto
print(f"o consumo medio do caroo é de {consumo_medio:.2f} km")