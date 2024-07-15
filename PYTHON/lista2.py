n = [6,9,3,5,8,2]
print(len(n))

n.append(7.4)
n.append(8.2)
n.append(5.3)
n.append(9.8)
n.append(2.7)

print(n)

n.pop()
n.pop()
print(n)

lista_ordenada = sorted(n)
print("Ordenado",lista_ordenada)

print(min(n))
print(max(n))

print(sum(n))
media = (sum(n))/(len(n))
print(media)

n.insert(0,'A')
n.insert(1,'B')

print(n)
















