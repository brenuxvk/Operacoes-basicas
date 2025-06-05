import random

notas = [0] * 4
i = 0

while i < 4:
    notas[i] = random.randint(0, 10)
    i += 1

media = sum(notas) / 4

print("Notas:", notas)
print("Média:", media)

if media >= 6:
    print("Aprovado")
elif media >= 4:
    print("Recuperação")
else:
    print("Reprovado")
