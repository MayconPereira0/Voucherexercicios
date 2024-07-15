numsi=[]
pares=[]
impares=[]

i = 0

while i < 20:
    nums = int(input("Digite 20 números:"))
    numsi.append(nums)
    if nums % 2 == 0:
        pares.append(nums)
    elif nums % 2 != 2:
        impares.append(nums)
    i += 1

print("Os números foram:",nums,"\n Os números pares:",pares,"\n Os números ímpares:",impares)