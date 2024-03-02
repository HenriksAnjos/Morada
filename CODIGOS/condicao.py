faturamento = 1000
custo = 8100

lucro = faturamento - custo

if lucro >=  0: # < tab > tudo o que voce quer que aonteca se a condiçao for VERDADEIRA
    print("lucro", lucro)   

else: # tudo o que voce quer que aconteça se a condiçao for FALSA
    print("PrejuizO!!!", lucro)

 
    
vendas = 17000
    
if vendas > 5000:
    bonus = 500
elif vendas > 10000:
    bonus = 150
elif vendas > 5000:
    bonus = 50
else:
    bonus = 0



# Acima de 15000 -> 500 de bonus
# Acima de 10000 -> 150 de bonus
# Acima de 5000 -> 50 de bonus
# Vendas da empresa > 50000

vendas = 17000
vendas_empresa = 40000
meta_empresa = 50000

if not vendas_empresa > meta_empresa:
    bonus = 0
else:  
    if vendas > 15000 and vendas_empresa > meta_empresa:
        bonus = 500
    elif vendas > 10000 and vendas_empresa > meta_empresa:
        bonus = 150
    elif vendas > 5000 and vendas_empresa > meta_empresa:
        bonus = 50
    else:
        bonus = 0

print("Bonus", bonus)

