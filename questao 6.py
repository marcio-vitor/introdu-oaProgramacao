

medias = []  
aprovados = 0
reprovados = 0

for i in range(1, 11):  
    print(f"\nAluno {i}:")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))

    media = (n1 + n2 + n3) / 3
    medias.append(media)

    if media >= 6:
        aprovados += 1
    else:
        reprovados += 1


maior_media = max(medias)
menor_media = min(medias)

print("\n===== RESULTADOS =====")
for i, m in enumerate(medias, start=1):
    print(f"Aluno {i} - Média: {m:.2f}")

print(f"\nMaior média: {maior_media:.2f}")
print(f"Menor média: {menor_media:.2f}")
print(f"Alunos aprovados: {aprovados}")
print(f"Alunos reprovados: {reprovados}")
