def e_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado = resultado * i
    return resultado

while True:
    print("\n=== MENU ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Par ou Ímpar")
    print("6 - Número Primo")
    print("7 - Fatorial")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Tchauu Obrigaduu!...")
        break

    if opcao == "1":
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print("Resultado da soma:", n1 + n2)
    else:
        if opcao == "2":
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
            print("Resultado da subtração:", n1 - n2)
        else:
            if opcao == "3":
                n1 = int(input("Digite o primeiro número: "))
                n2 = int(input("Digite o segundo número: "))
                print("Resultado da multiplicação:", n1 * n2)
            else:
                if opcao == "4":
                    n1 = int(input("Digite o primeiro número: "))
                    n2 = int(input("Digite o segundo número: "))
                    if n2 != 0:
                        print("Resultado da divisão:", n1 / n2)
                    else:
                        print("Erro: divisão por zero!")
                else:
                    if opcao == "5":
                        n = int(input("Digite um número: "))
                        if n % 2 == 0:
                            print(n, "é Par")
                        else:
                            print(n, "é Ímpar")
                    else:
                        if opcao == "6":
                            n = int(input("Digite um número: "))
                            if eh_primo(n):
                                print(n, "é Primo")
                            else:
                                print(n, "não é Primo")
                        else:
                            if opcao == "7":
                                n = int(input("Digite um número: "))
                                print("Fatorial de", n, "=", fatorial(n))
                            else:
                                print("Opção inválida! Tente novamente.")
