from data import dataset
from task1 import *
from task2 import *

#Рекурсивна функція, що повертає дати, у які різні люди робили покупки

def recursionByProducts(user_tels = list(dataset.keys()), d = {}, amount_of_products = 0):
    if user_tels == []:
        return d
    user_tel = user_tels[0]
    day_list = list(dataset[user_tel]['days'].keys())
    for i in range(len(day_list)):
        day = day_list[i]
        a = str(dataset[user_tel]['days'][day])
        b = a.split()
        amount_of_products += len(b)
    d[user_tel] = amount_of_products
    return recursionByProducts(user_tels[1:], d, amount_of_products = 0)

#Рекурсивна функція, що повертає кількість продуктів, яку купила кожна людина

def recursionByUsers(user_tels = list(dataset.keys()), result_dict = dict()):
    if user_tels == []:
        return result_dict
    user_tel = user_tels[0]
    days_list = dataset[user_tel]['days'].keys()
    result_dict.update({user_tel: set(days_list)})
    return recursionByUsers(user_tels[1:], result_dict)

print("Task 3")

result = recursionByUsers()
print(result)
res = recursionByProducts()
print(res)
print("\n\n")



