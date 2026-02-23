total_pedidos = 0
total_itens = 0
valor_total_dia = 0.0
maior_pedido = 0.0
clientes_acima_3_itens = 0

continuar = "sim"

while continuar.lower() == "sim":
    total_pedidos += 1
    print(f"\n----- Pedido {total_pedidos} -----")

    itens_pedido = int(input("Quantos itens o cliente vai comprar? "))

    if itens_pedido > 3:
        clientes_acima_3_itens += 1

    valor_pedido = 0.0

    for i in range(1, itens_pedido + 1):
        nome = input(f"Digite o nome do {i}º item: ")
        preco = float(input(f"Digite o preço de {nome}: R$ "))
        valor_pedido += preco
        total_itens += 1

    print(f"Valor total deste pedido: R${valor_pedido:.2f}")
    valor_total_dia += valor_pedido

    if valor_pedido > maior_pedido:
        maior_pedido = valor_pedido

    continuar = input("\nDeseja registrar outro pedido? (sim/não) ")

print("\n===== RESUMO DO DIA =====")
print(f"Total de pedidos realizados: {total_pedidos}")
print(f"Total de itens vendidos: {total_itens}")
print(f"Valor total arrecadado: R${valor_total_dia:.2f}")
print(f"Maior valor de pedido registrado: R${maior_pedido:.2f}")
print(f"Número de clientes que comprou mais de 3 itens: {clientes_acima_3_itens}")