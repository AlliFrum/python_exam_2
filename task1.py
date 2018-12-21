from data import dataset

#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник
#   Викликати функцію


def addUserProduct(user_tel, product_name, day):

        if user_tel in dataset:
            if day in dataset[user_tel]["days"]:
                prods_list = list(dataset[user_tel]['days'][day])
                prods_list.append(product_name)
                dataset[user_tel]['days'][day] = set(prods_list)
            else:
                dataset[user_tel]['days'][day] = product_name
        else:
            dataset[user_tel] = {}
            dataset[user_tel]['days'] = {day: product_name}
            name = input("Enter the name of new human ")
            dataset[user_tel]['name'] = name

print("Task 1")

#Додати нового користувача та нову покупку
addUserProduct("123-1234", "coffee", "12.12.2014")

#Додати існуючому користувачу нову покупку в новий день
addUserProduct("112-4556", "coffee", "21.02.2012")

#Додати існуючому користувачу нову покупку в існуючий день
addUserProduct("221-6554", "bananas", "12.12.2012")

print(dataset)


print("\n\n")