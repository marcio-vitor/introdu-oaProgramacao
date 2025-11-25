senha=0
senha = int(input("Digite a senha: "))
if senha == 1234:
    print("acesso permitido")
while senha != 1234:
    print("senha incorreta, tente novamente")
    senha = int(input("digite a senha:"))
    if senha ==1234:
            print ("acesso permitido")