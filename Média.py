import random

def main():

 notas = [0.0] * 4
 i = 0

 while i < 4:
    notas[i] = random.uniform(0.0, 10.0)
    i += 1
 i= 0 
 media = 0.0
 while i < 4:
  media += notas[i]
  i += 1
 media /= 4.0

 print(f"O Eduard tirou {notas[0]:,.2} na primeira prova {notas[1]:,.2} na segunda prova {notas[2]:,.2} na terceira prova {notas[3]:,.2} na quarta prova e sua media foi media {media:,.2}")

 if media >= 6.0:
    print("Aprovado")
 elif media >= 4.0:
    print("Recuperação")
 else:
    print("Reprovado")

 return 0 
main()