
# Lista de produtos
disc_precos = {"iphone": 1500, "ipad": 1000, "visonpro": 3500, "macbook": 10000}


#  Buscar especifico item na lista
preco_produto = disc_precos["macbook"]
print(preco_produto)

# Editar preço ou adicionar item a lista
disc_precos["airpod"] = 2000
print(disc_precos)

# Deletar um item da lista 
disc_precos.pop("airpod")
print(disc_precos)

# Quantidade de produtos na lista
print(len(disc_precos))

# Buscar lista de itens e valores
print("macbook" in disc_precos) #true/false
print(disc_precos.values()) #valores 
print(disc_precos.keys())  #itens

