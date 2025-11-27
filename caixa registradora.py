print("=== Caixa Registradora ===")

total = 0
quantidade = 0
mais_caro = 0

continuar = "s"

while continuar == "s":

    preco = -1
    while preco < 0:
        preco = float(input("Preço do produto: R$ "))
        if preco < 0:
            print("Preço inválido! Digite um valor positivo.")

    total = total + preco
    quantidade = quantidade + 1

    if preco > mais_caro:
        mais_caro = preco

     
    continuar = ""
    while continuar != "s" and continuar != "n":
        continuar = input("Deseja adicionar outro produto? (s/n): ").lower()

    
        if continuar != "s":
            if continuar != "n":
                print("Digite apenas s ou n.")
                continuar = ""  

 
print("\n=== Resumo da compra ===")
print("Total: R$ " + str(round(total, 2)))
print("Quantidade de produtos: " + str(quantidade))
print("Média: R$ " + str(round(total / quantidade, 2)))
print("Produto mais caro: R$ " + str(mais_caro))
