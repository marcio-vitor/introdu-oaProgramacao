n = int(input("1 numero: "))
c = 0
for i in range(1, n+1):
    if n%i==0:
       c+=1
if c<=2:
    print("primo")
else:
    print("nn")