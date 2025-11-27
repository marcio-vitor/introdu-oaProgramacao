print("=== Analisador de Dados Ambientais ===")

N = int(input("Quantas leituras de temperatura serão analisadas? "))

soma = 0
acima_30 = 0
abaixo_15 = 0

for i in range(N):

    numero = i + 1
    print("Digite a temperatura " + str(numero) + ":")
    temp = float(input())

    if i == 0:
        maior = temp
        menor = temp
    else:
        if temp > maior:
            maior = temp
        if temp < menor:
            menor = temp

    soma = soma + temp

    if temp > 30:
        acima_30 = acima_30 + 1

    if temp < 15:
        abaixo_15 = abaixo_15 + 1


media = soma / N

print("\n=== RESULTADOS ===")
print("Maior temperatura: " + str(maior) + " °C")
print("Menor temperatura: " + str(menor) + " °C")
print("Média das temperaturas: " + str(round(media, 2)) + " °C")
print("Acima de 30 °C: " + str(acima_30))
print("Abaixo de 15 °C: " + str(abaixo_15))

diferenca = maior - menor

if diferenca > 20:
    print("ALERTA: Variação térmica extrema!")
else:
    print("Variação dentro do esperado.")
