qnt_num = int(input("Digite uma certa quantidade:"))
nums = []

while qnt_num > len(nums):
    nums.append(int(input("Digite um número:")))
print(nums)
print(f"O maior número da lista é:", {max(nums)})
