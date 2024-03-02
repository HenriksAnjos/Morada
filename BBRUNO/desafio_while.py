'''
#Descobrisse quantas pessoas moraram no manoel
#Quanto tempo cada morador morou no Manoel ( meses )


moradores_monoel = {"bruno mineiro":[ 20], "henrique": [24], "mirkon": 8, "bruno castro": 7}

#pedir o input para o usuário
morador = input("Digite nome do morador:")
morador = morador.lower()

#Se o morador for encontrado, imprime a mensagem "Morador: {morador} \n Morou {meses} meses na residencia do Sr.Manoel"
if morador in moradores_monoel:
  meses = moradores_monoel[morador]
  print(f"Morador: {morador} \n Morou {meses} meses na residencia do Sr.Manoel")

#Senão pedimos novamente o input para o usuário
else:
  print("Morador nao encontrado")
'''
#Booleano => True, False
#Boolean

#Inicializando as variáveis
moradores_monoel = {"bruno mineiro":20, "henrique": 24, "mirkon": 8, "bruno castro": 7}
morador_nao_encontrado = True

#While (Enquanto) nenhum morador for encontrado, repete o processo de pedir pelo input do usuário e validar novamente
while(morador_nao_encontrado):
  
  morador = input("Digite nome do morador:")
  morador = morador.lower()

  #Se o morador for encontrado, imprime a mensagem "Morador: {morador} \n Morou {meses} meses na residencia do Sr.Manoel"
  if morador in moradores_monoel:
    morador_nao_encontrado = False
    meses = moradores_monoel[morador]
    print(f"Morador: {morador} \n Morou {meses} meses na residencia do Sr.Manoel")

  #Senão pedimos novamente o input para o usuário
  else:
    print("Morador nao encontrado")

print('Programa encerrado')

