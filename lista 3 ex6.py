maiorMedia=0
menorMedia=999
qtdeap=0
qtderep=0
for i in range(10):
    nota1=float(input("digite a primeira nota: "))
    nota2=float(input("digite a segunda nota: "))
    nota3=float(input("digite a terceira nota: "))
    media=(nota1+nota2+nota3)/3
    if media>maiorMedia:
            maiorMedia=media
    if media<menorMedia:
            menorMedia=media
    if media >=6:
            qtdeap+=1
else:
    qtderep+=1
print("a maior media foi",maiorMedia)
print("a menor media foi",menorMedia)
print("a quantidade de alunos aprovados foi",qtdeap)
print("a quantidadse de reprovados foi",qtderep)