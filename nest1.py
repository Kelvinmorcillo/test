print("Você realmente gosta de TV? ")
tvShow = input("Qual é o sua série preferida? ")
if tvShow == "24 horas":
  print("Melhor serie de todos os tempos")
  faveCharacter = input("E quem é o seu personagem favorito? ")
  if faveCharacter == "jack bauer":
      print("Logico que é ele WHERE'S THE BOMB? e qual é o nome da filha dele então? ")
      filha = input("e qual é o nome da filha dele então? ")
      if filha == "kim":
          print("Aí Sim, ela mesma")
      else:
          print("Nah,Jack Bauer é o melhor")
  else:
      print("Nah,Jack Bauer é o melhor")
          
elif tvShow == "friends":
  print("Credo")
else:
  print("ah ta")