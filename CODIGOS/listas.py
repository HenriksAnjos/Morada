vendas = [100, 50, 130, 80, 120, 200]
produtos = ["iphone", "ipad", "airpod"]

print(vendas[0])

total_vendas = sum(vendas)
print(total_vendas)
quantidade = len(vendas)
print(quantidade)
valor_max = max(vendas)
valor_min = min(vendas)
print(valor_max, valor_min)

posicao = vendas.index(130)
print(posicao)

print(vendas[2:])

produtos = ["iphone", "ipad", "airpod"]
precos = [4000, 8000, 2000]

print("iphone" in produtos)
precos[0] = precos[0] * 1.1
print(precos)

# Adicionar item
produtos.append("macbook")
precos.append(10000)
print(produtos)
print(precos)

# Remover Item
produtos.remove("macbook")
precos.pop(-1)
print(produtos)
print(precos)

# Insirir um valor
produtos.insert(1, "airpod")
print(produtos)

# Contar valores
print(produtos.count("airpod"))

# Ordenar
precos.sort() # (reverse=true) 
print(precos)
