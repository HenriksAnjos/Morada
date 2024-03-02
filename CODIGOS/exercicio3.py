

disc_precos = {"iphone": 1500, "ipad": 1000, "visionpro": 3500, "macbook": 10000}


produto_procurado = input("Digite nome do produto:")
produto_procurado = produto_procurado.lower()

if produto_procurado in disc_precos:
  preco = disc_precos[produto_procurado]
  print(f"Produto: {produto_procurado} \n $ {preco*1.0}")

else:
  print("Produto nao encontrado, tente novamente") 

