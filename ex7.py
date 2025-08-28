T = 1.5
h = 1.1
anos = 0
for i in range(10000000000000):
    T += 0.2
    h += 0.3
    if h>T: 
        break
    else:
        anos += 1
print(anos)