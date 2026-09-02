glicose = float(input("Digite a medida da glicose: "))
if glicose < 100:
    print("Glicose normal") 
elif glicose >= 100 and glicose <= 140:
    print("Glicose alterada")
else:
    print("Diabetes")