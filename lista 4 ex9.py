número=int(input("Digite um número: "))
cont=0
divisor=1
while divisor<=número:
    if número%divisor==0:
        cont+=1
    divisor+=1
if cont==2:
    print("o número e primo!")
else:
    print("o número não e primo")