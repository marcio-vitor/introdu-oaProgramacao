#Escreva um algoritmo que leia 20 valores inteiros e ao final exiba a soma dos n´umeros positivos e a quantidade de valores negativos.
i=1
SomaPositivos=0
ContNeg=0
while i<=20:
    valor=int(input("Digite o valor: "))
    if valor>=0:
        SomaPositivos+=valor
    else:
        ContNeg+=1
    i+=1
print("A soma dos numeros positivo é",SomaPositivos)
print("A quantidade dos numeros negativos é",ContNeg)
