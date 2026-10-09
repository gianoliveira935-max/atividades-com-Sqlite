while True:
    try:
        temperatura = float(input("Digite a temperatura: "))
        break
    except ValueError:
        print("Valor inválido. Digite apenas números para a temperatura.")

while True:
    escala = input("Digite a escala (C/F): ").strip().upper()
    if escala in ["C", "F"]:
        break
    print("Escala inválida. Digite apenas C ou F.")

if escala == "C":
    convertido = (temperatura * 9 / 5) + 32
    print(f"{temperatura}°C equivale a {convertido:.2f}°F")
elif escala == "F":
    convertido = (temperatura - 32) * 5 / 9
    print(f"{temperatura}°F equivale a {convertido:.2f}°C")