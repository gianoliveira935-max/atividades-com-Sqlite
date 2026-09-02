valor_unitario = float(input("digite o valor do produto: "))
quantidade = int(input("digite a quantidade do produto: "))
dinheiro_recebido = float(input("digite o valor recebido do cliente: "))

valor_total = valor_unitario * quantidade
if dinheiro_recebido >= valor_total:
    troco = dinheiro_recebido - valor_total
    print(f"Troco: R$ {troco:.2f}")
else:
    print("Valor recebido é insuficiente.")