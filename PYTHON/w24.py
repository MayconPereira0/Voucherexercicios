soma3 = 0
soma5 = 0
for i in range(1,1000):
    if i % 3 == 0:
        soma3 += i
    
    if i % 5 == 0:
        soma5 += i

print(soma3,soma5)