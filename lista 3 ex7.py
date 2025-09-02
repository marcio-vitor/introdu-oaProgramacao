thanos=1.50
miranha=1.10
for i in range(1000):
    if miranha>thanos:
        break
    thanos+=0.02
    miranha+=0.03
print("vai demorar ",i,"anos para que o miranha seja maior que o thanos!")