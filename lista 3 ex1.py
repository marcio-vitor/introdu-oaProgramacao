somaPos=0
ContNeg=0
for i in range(20):
    valor=int(input("Digite o valor: "))
    if valor>=0:
        somaPos+=valor
    else:
        ContNeg+=1
print("A soma dos numeros positivo é",somaPos)
print("A quantidade dos numeros negativos é",ContNeg)