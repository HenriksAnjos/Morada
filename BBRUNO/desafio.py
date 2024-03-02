#Descobrisse quantas pessoas moraram no manoel
#Quanto tempo cada morador morou no Manoel ( meses )


moradores_monoel = {"bruno ": 20, "henrique": 24, "mirkon": 8, "bruno castro": 7}
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

  morador = input("Digite nome do morador:")
  morador = morador.lower()

