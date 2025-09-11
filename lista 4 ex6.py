maiorMedia=0
menorMedia=999
qtdeap=0
qtderep=0
aluno=0
i=0
while aluno<10:
    nota1=float(input("digite a primeira nota: "))
    nota2=float(input("digite a segunda nota: "))
    nota3=float(input("digite a terceira nota: "))
    aluno+=i+1
    media=(nota1+nota2+nota3)/3
    print("A media do aluno ",aluno,"é :",media)
    if media>maiorMedia:
            maiorMedia=media
    if media<menorMedia:
            menorMedia=media
            qtderep+=1
    if media >=6:
            qtdeap+=1
            print("aluno aprovado")
    else:
        print("aluno reprovado")
print("a maior media foi",maiorMedia)
print("a menor media foi",menorMedia)
print("a quantidade de alunos aprovados foi",qtdeap)
print("a quantidadse de reprovados foi",qtderep)