nome = "luiz henrique anjos"
email = "henriks@hotmail.com.br"

# 1 Exercicio - descubra o servidor do email

posicao = email.find("@")
servidor = email[posicao:]
print(servidor)

# 2 Exercicio - Pegar primeiro nome do usuario

posicao = nome.find(" ")
primeiro_nome = nome[:posicao]
print(primeiro_nome)

# 3 Exercicio - Construa uma mensagem: usuario primeiro_nome cadastrado com sucesso com o email tal

mensagem = f"usuario {primeiro_nome} cadastrado com sucesso com o email: {email}"
print(mensagem)

# 4 Exercicio - Construa uma mensagem: Enviamos um link de confirmaçao para o email j***@gmail.com
primeira_letra = email[0]
mensagem2 = f"Enviamos um link de confirmaçao para o email {primeira_letra}******{servidor}"
print(mensagem2)
