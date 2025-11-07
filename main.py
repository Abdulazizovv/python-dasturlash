
# ismni harflarini listga chiqarish
# ism = input("Ismingizni kiriting:>")

# letters = []

# for i in ism:
#     letters.append(i)

# print("Natija: ", letters)

# listdagi takrorlangan elementlarni o'chirish

lst = [1, 2, 2, 3, 4, 4, 5, 5]

new_list = []

for i in lst:
    if i in new_list == False:
        new_list.append(i)

print("Natija: ", new_list)