num_secreto = 67

while True:
    try:
        chute = int(input("Adivinhe o número: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if chute > num_secreto:
        print("Seu número é menor")
    elif chute < num_secreto:
        print("Seu número é maior")
    else:
        print("Acertou!!! 🎉")
        break