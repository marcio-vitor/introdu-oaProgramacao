
n = int(input("Digite o número de jogadores: "))
    
    
soma_alturas = 0
    
    
for i in range(n):
    altura = float(input(f"Digite a altura do jogador {i+1}: "))
soma_alturas += altura
    
    
altura_media = soma_alturas / n
    
    
print(f"A altura média do time é: {altura_media:.2f} metros")


