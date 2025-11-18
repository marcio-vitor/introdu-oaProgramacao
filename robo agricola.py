#robo agricola
bateria = int(input("Nível de bateria (0 a 100): "))
temperatura = float(input("Temperatura do ambiente (°C): "))
umidade = int(input("Umidade do solo (0 a 100): "))
modo = input("Modo de operação (plantio, colheita ou irrigacao): ")

#bateria
if bateria < 20:
    print("Bateria muito baixa! Retorne imediatamente para a base.")

if bateria >= 20:
    if bateria < 50:
        print("Atenção: bateria em nível moderado.")

if bateria >= 50:
    print("Bateria suficiente para operação.")
#temperatura
if temperatura > 40:
    print("Temperatura crítica! Operação suspensa.")

if temperatura < 5:
    print("Frio extremo! Modo de economia ativado.")
#umidade
if umidade < 30:
    print("Solo muito seco. Recomendado iniciar irrigação.")

if umidade > 80:
    print("Solo encharcado! Suspenda irrigação imediatamente.")
#modo
if modo == "plantio":
    print("Iniciando modo PLANTIO...")

if modo == "colheita":
    print("Iniciando modo COLHEITA...")

if modo == "irrigacao":
    print("Iniciando modo IRRIGAÇÃO...")

bateria_ok = 0
temperatura_ok = 0
umidade_ok = 0

if bateria >= 50:
    bateria_ok = 1

if temperatura >= 10:

    if temperatura <= 35:
        temperatura_ok = 1

if umidade >= 30:

    if umidade <= 80:
        umidade_ok = 1

if bateria_ok == 1:
    if temperatura_ok == 1:
        if umidade_ok == 1:
            print("Robô autorizado a iniciar a operação!")

if bateria_ok != 1:
    print("Operação negada! Verifique as condições do ambiente.")

if bateria_ok == 1:
    if temperatura_ok != 1:
        print("Operação negada! Verifique as condições do ambiente.")

if bateria_ok == 1:
    if temperatura_ok == 1:
        if umidade_ok != 1:
            print("Operação negada! Verifique as condições do ambiente.")
