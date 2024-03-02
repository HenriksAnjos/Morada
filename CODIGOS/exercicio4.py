
# Regra do imposto
# Preço ate 1000 -> imposto e de 10%
# Preço maior do que 1000 -> imposto e de 15% 

lista_precos = [1500, 1000, 800, 2000]

for preco in lista_precos:
    if preco > 1000:
       imposto = preco * 0.15
    else:
        imposto = preco * 0.1
    print(f"Preço: {preco}, Imposto: {imposto}")