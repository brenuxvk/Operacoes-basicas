
def main():
    num1 = 1
    num2 = 2
    
    print("Hello, World!", num1)
    print("Hello, World!", num2)

    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))

    print("A soma dos números é:", num1 + num2)

    soma = num1 + num2
    multi = num1 * num2
    sub = num1 - num2

    if num2 == 0:
        print("Não é possível dividir por zero")
        div = "indefinido"
    else:
        div = num1 / num2
    
    print("A soma de", num1, "+", num2, "=", soma)
    print("A multiplicação", num1, "*", num2, "=", multi)
    print("A divisão", num1, "/", num2, "=", div)
    print("A subtração", num1, "-", num2, "=", sub)

    return 0

if __name__ == "__main__":
    main()
    print("Fim do programa")
