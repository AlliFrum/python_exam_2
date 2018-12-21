
"""
    Написати валідатор ....
    Правило валідації
"""

import re


def getUserTel():

    user_input = input("Enter tel")

    if (re.match(r"^\d{3}-\d{4}$", user_input) ):
        return user_input
    else:
        return False


"""
    Написати валідатор ....
    Правило валідації
"""


def getProductName():
    user_input = input("Enter product")
    if (re.match(r"^[a-z]{1,10}$", user_input)):
        return user_input
    else:
        return False

"""
    Написати валідатор ....
    Правило валідації
"""


def getDay():
    user_input = input("Enter day")
    if (re.match(r"^\d{2}\.\d{2}\.\d{4}$", user_input)):
        return user_input
    else:
        return False
