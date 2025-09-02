somaAltura=0
qtdejog=int(input("digite a quantidade de jogador: "))
for i in range(qtdejog):
    altura=float(input("digite a altura do jogador: "))
    somaAltura+=altura
    media=somaAltura/qtdejog
print("a media de altura dos jogadores é ",media)