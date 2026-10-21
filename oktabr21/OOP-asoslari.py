# vorislik(inheritance)

# DRY (Don't Repeat yourself)


# Polymorphism - nomi bir xil lekin vazifasi turli xil metodlar


# class Parent:

#     def move(self):
#         print("Yuryabdi")


# class Car(Parent):
#     pass


# class Boat(Parent):

#     def move(self):
#         print("Suzyabdi")


# car1 = Car()
# boat1 = Boat()

# car1.move()
# boat1.move()





# Encapsulation(Inkapsulatsiya) - Ma'lumotlarni class ichida himoya qilish

class BankAccount:

    def __init__(self):
        self.__balance = 150 # Private

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount < 0:
            print("Mumkin bo'lmagan qiymat")
            return
        self.__balance += amount
        return self.__balance


umarxon = BankAccount()
umarxon.set_balance(200)
print(umarxon.get_balance())
