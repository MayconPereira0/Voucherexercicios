snums = 0
cont = 0
nums_text = ""

while cont < 5:
    nums = int(input("Digite os números:"))
    snums += nums
    nums_text += str(nums) + "\n"
    cont += 1

print(snums)

print("Números digitados:")
print(nums_text.strip())
