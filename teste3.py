usuario="admin"
pwd="1234"
nome=input("Digite seu nome:")
senha=int(input("digite sua senha:"))
if nome==usuario:
    if pwd==senha:
        print("login realizado com sucesso!")
    else:
        print("senha incorreta!")
else:
    print("usuario inexistente!")
