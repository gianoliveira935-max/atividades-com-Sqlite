temperatura = (input("vocce vai digitar a temperatura em c ou f? (c/f): "))
if temperatura == "c":
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
elif temperatura == "f":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"A temperatura em Celsius é: {celsius:.2f}°C")


