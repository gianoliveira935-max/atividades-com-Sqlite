preço_unitário = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade de produtos: "))

total_da_compra = preço_unitário * quantidade
print(f"O valor total da compra é: R$ {total_da_compra:.2f}")

troco_cliente = float(input("Digite o valor pago pelo cliente: ")) - total_da_compra
print(f"O troco a ser devolvido é: R$ {troco_cliente:.2f}")