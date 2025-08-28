maior = 0
menor = 0
ap = 0
rep = 0
for i in range(10):
    n1 = float(input("n1"))
    n2 = float(input("n2"))
    n3 = float(input("n3"))
    media = (n1+n2+n3) / 3
    if media>=6:
        ap+=1
    else:
        rep+=1
    if media>maior:
        maior=media
    elif media<menor:
        menor=media
print(maior, menor, ap, rep)