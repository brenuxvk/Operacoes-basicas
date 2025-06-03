def main():
  idade  = -1

  while idade < 0:
    idade = int(input("Digite sua idade: "))
    if idade < 0:
      print("idade inexistente, digite novamente: \n")
      print("Idade invalida")
  
  if idade < 5:
   if idade < 0:
    print("Idade invalida")
  
    print("Voce está na creche")
  elif idade >= 5 and idade <= 10:
   print("Voce está no ensino fundamental(1° ao 5° ano)")
  elif idade >= 11 and idade <= 16:
   print("Voce está no ensino medio (6° ao 9° ano)")
  elif idade >= 15 and idade <= 18:
   print("Voce está no ensino medio (1° ao 3° ano)")
  else:
   print("Você está fora da escola")
  return 0 

main()

