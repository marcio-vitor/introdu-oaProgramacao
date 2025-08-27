thanos = 150
homem_aranha = 110

crescimento_thanos = 2
crescimento_aranha = 3

anos = 0

while homem_aranha <= thanos:
    thanos += crescimento_thanos
    homem_aranha += crescimento_aranha
    anos += 1

print("Serão necessários", anos, "anos para que o Homem-Aranha seja maior que o Thanos.")
print("Altura final do Homem-Aranha:", homem_aranha, "cm")
print("Altura final do Thanos:", thanos, "cm")
print("Ao pó retornarei!!! Aranha, Homem")
