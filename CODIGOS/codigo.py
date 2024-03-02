faturamento = 1200 #numero inteiro -> int
custo = 770

novas_vendas = 300
faturamento = faturamento + novas_vendas

taxa_imposto = 0.1 #numero decimal -> float
mensagem = "O faturamento foi de " # string = texto
teve_lucro = False # boolean

imposto = taxa_imposto * faturamento
print("faturamento", faturamento)
print("custo", custo)
print("lucro", faturamento - custo - imposto) 
print(mensagem, faturamento)