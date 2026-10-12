

# TypeError - tiplar bo'yicha xatolik
# a = 5 + "s"

# print(a)


# ValueError - Qiymat xatoligi

# a = int("555")
# print(a)


# IndexError - index bo'yicha xatolik ya'ni yo'q indeksga murojaat

# ismlar = ["Muhammadaziz", "Umarxon", "Muhammadsafo"]
# print(ismlar[4])


# ZeroDivisionError - sonni 0 ga bo'lgandagi xatolik

# a = int(input("1-son:>>"))
# b = int(input("2-son:>>"))


# try:
#     natija = a / b
#     print(natija)
# except:
#     print("0 ga bo'lib bo'lmaydi")

# NameError - nom bo'yicha xatolik

# name = "Umarxon"
# print(ism)


try:
    if 5>6:
        print("asdf")
except ZeroDivisionError:
    print("Nolga bo'lib qo'ydingiz")
except NameError:
    print("Nima buuu")
except SyntaxError:
    print("Hechqisi yo'q bu xatolik dasturchi tomonidan qilingan")