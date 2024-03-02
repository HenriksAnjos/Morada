faturamento = 1000
custo = 700 

lucro = faturamento - custo

#print(f"faturamento: {faturamento}, custo: {custo}, Lucro; {lucro}")
#print("faturamento:" + str(faturamento) + ", custo: " + str(custo) + ", Lucro: " + str(lucro))

email = "email_falso@gmail.com"

print(email.lower())
print(email.find("@")) # -1 se ele nao encontrar o elemento

posicao = email.find("@")
servidor = email[posicao+1:]
print(servidor)

# tamanho de um texo
tamanho = len(email)
print(tamanho)

# trocar um pedaço do texo
email_trocado = email.replace("gmail.com","hotmail.com" )
print(email_trocado)

nome = "joao lira"
print(nome.capitalize()) # joao lira
print(nome.title()) # joao Lira

# especiais - formaçao numerico
margem = lucro / faturamento
print(f"faturamento: R${faturamento:,.2f}\n custo: {custo}\n Lucro; {lucro}") # \n enter
print(f"margem: {margem:.1%}")
