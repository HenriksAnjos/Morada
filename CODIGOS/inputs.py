nome = input("Digite aqui seu nome:")
email = input("Digite aqui seu email:")

posicao = email.find("@")
servidor = email[posicao:]
print(servidor)

posicao = nome.find(" ")
primeiro_nome = nome[:posicao]
print(primeiro_nome)

mensagem = f"usuario {primeiro_nome} cadastrado com sucesso com o email: {email}"
print(mensagem)

primeira_letra = email[0]
mensagem2 = f"Enviamos um link de confirmaçao para o email {primeira_letra}******{servidor}"
print(mensagem2) 