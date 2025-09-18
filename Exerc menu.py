import os
print("********** OPERAÇÕES MATEMATICA **********")
print("Escolha uma das opções abaixo: ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Par ou Impar")
print("6 - Primo")
print("7 - Fatorial")
opção=input("Digite a opção desejada ou <SAIR> para encerrar: ")
opçaoMaiusc=opção.upper()
while opçaoMaiusc!="SAIR":
    if opção=="1":
        numero1=int(input("Digite o primeiro valor: "))
        numero2=int(input("Digite o segundo valor: "))
        print("O resultado da soma entre",numero1,"e",numero2,"é",numero1+numero2)
    if opção=="2":
        numero1=int(input("Digite o primeiro valor: "))
        numero2=int(input("Digite o segundo valor: "))
        print("O resultado da subtração entre",numero1,"e",numero2,"é",numero1-numero2)
    if opção=="3":
        numero1=int(input("Digite o primeiro valor: "))
        numero2=int(input("Digite o segundo valor: "))
        print("O resultado da multiplicação entre",numero1,"e",numero2,"é",numero1*numero2)
    if opção=="4":
        numero1=int(input("Digite o primeiro valor: "))
        numero2=int(input("Digite o segundo valor: "))
        print("O resultado da divisão entre",numero1,"e",numero2,"é",numero1/numero2)
    if opção=="5":
        numero1=int(input("Digite um número: "))
        if numero1 % 2 == 0:
            print(numero1, "é Par")
        else:
            print(numero1, "é Ímpar")
    if opção=="6":
        numero1=int(input("Digite um número: "))
        c = 0
        for i in range(1, numero1+1):
            if numero1%i==0:
                c+=1
        if c<=2:
            print("primo")
        else:
            print("não e primo")
    if opção=="7":
        numero1=int(input("1 número "))
        fatorial = 1
        for i in range(1, numero1+1):
            fatorial = fatorial*i
        print(fatorial)
    input("Pressione ENTER para voltar ao MENU!")
    os.system("cls")
    print("Escolha uma das opções abaixo: ")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Par ou Impar")
    print("6 - Primo")
    print("7 - Fatorial")
    opção=input("Digite a opção desejada ou <SAIR> para encerrar: ")
    opçaoMaiusc=opção.upper()



