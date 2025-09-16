thanos=1.50
miranha=1.10
i=0
while miranha<thanos:
    if thanos>miranha:
        i+=1
    thanos+=0.02
    miranha+=0.03
else:
    print("vai demorar ",i,"anos para que o miranha seja maior que o thanos!")
    print(f"A altura do miranha:",miranha)
    print(f"A altura do thanos:",thanos)
    breakpoint