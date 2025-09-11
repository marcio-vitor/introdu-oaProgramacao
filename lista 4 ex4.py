somaAltura=0
qtdejog=int(input("digite a quantidade de jogador: "))
contador=0
while contador<qtdejog:
    altura=float(input("digite a altura do jogador: "))
    somaAltura+=altura
    media=somaAltura/qtdejog
    contador+=1
print("a media de altura dos jogadores é ",media,"metros")