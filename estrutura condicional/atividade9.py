produtos = ["Arroz", "Feijão", "Macarrão", "Açúcar", "Sal"]
precos = [5.00, 3.50, 4.80, 8.90, 7.32]

print("Lista de produtos:")

for i in range(len(produtos)):
    print(f"{i + 1} - {produtos[i]} - R$ {precos[i]:.2f}")

codigo = int(input("Codigo do produto comprado: "))
quantidade = int(input("Quantidade comprada: "))

preco = precos[codigo - 1]
valor = preco * quantidade

print(f"Valor a pagar: R$ {valor:.2f}")
