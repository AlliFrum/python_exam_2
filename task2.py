from data import dataset


#    Створити пакет validators та написати функції, що валідують усі дані. Імпорутвати дані функції.

from validators.lib import getUserTel, getProductName, getDay


from task1 import addUserProduct


#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник.
#   Усі дані вводить користувач. Використати валідатори. Викликати функцію

def addUserProductValidator():

    user_tel = getUserTel()
    while not user_tel:
        print("Wrong tel. Try again")
        user_tel = getUserTel()
    user_product = getProductName()
    while not user_product:
        print("Wrong product. Try again")
        user_product = getProductName()
    user_day = getDay()
    while not user_day:
        print("Wrong day. Try again")
        user_day = getDay()

    addUserProduct(user_tel, user_product, user_day)



print("Task 2")
addUserProductValidator()
print(dataset)


print("\n\n")