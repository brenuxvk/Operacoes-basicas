import random

def main():

    print("Jogo de adivinhação pela posição do vetor")
    notas = [0] * 30

    j = 0
    i = 0
    
    for i in notas:
        notas[j] = random.randint(1, 100)
        j += 1
    posiAleatorio = random.randint(0, 29)
    num = notas[posiAleatorio]
    posiEscolhida = 0 
    i = 0
    j = 0

    acerto = False
    while i < 10:
        posiEscolhida = int(input("Digite a posição do vetor: "))
        if posiEscolhida == posiAleatorio:
            print("Parabéns, você acertou! \n")
            acerto = True
            break
        elif posiEscolhida > posiAleatorio:
            print("Posição fica mais a esquerda \n")
        else:
            print("Posição fica mais a direita \n")
        i += 1
        print("Errou, você ainda tem", 10 - i, "tentativas \n")
       
    if acerto:
            print("Você acertou sobrando", 10 - i," tentativas \n")
    else:
        print("Você não acertou, o número era", num, "e estava na posição", posiAleatorio, "\n") 

    print(notas)

    return 0 
 
main() 