# Exercicio desafios
# sestema de consulta de preços

produtos = ["celular", "camera", "fone de ouvido", "monitor"]
precos = [1500, 1000, 800, 2000]


produto_procurado = input("Digite nome do produto:")
produto_procurado = produto_procurado.lower()

if produto_procurado in produtos:
   posicao = produtos.index(produto_procurado)
   preco = precos[posicao]
   print(f"Produto: {produto_procurado} \n R$ {preco*1.0}")
else:
   print("Produto nao encontrado, tente novamente")


