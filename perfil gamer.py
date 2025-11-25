#dados
horas = int(input("Horas por semana: "))
gasto = int(input("Gasto mensal: "))
jogos = int(input("Jogos instalados: "))

perfil = "não classificado"

#HARDCORE
if horas >= 30:
    if gasto >= 100:
        if jogos >= 20:
            perfil = "HARDCORE"
#INTERMEDIÁRIO (só se não for hardcore)
if perfil == "não classificado":
    if horas >= 10:
        if horas <= 29:
            if gasto >= 30:
                if gasto <= 99:
                    if jogos >= 10:
                        if jogos <= 19:
                            perfil = "INTERMEDIÁRIO"
#CASUAL (só se não for hardcore ou intermediário)
if perfil == "não classificado":
    # CASUAL se QUALQUER condição for verdadeira
    if horas < 10:
        perfil = "CASUAL"
    else:
        if gasto < 30:
            perfil = "CASUAL"
        else:
            if jogos < 10:
                perfil = "CASUAL"
print("Classificação:", perfil)
