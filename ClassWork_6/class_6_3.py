# Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції використати рядки документації DocStrings.

def findingBiggerNumber (a ,b):
    """Comparing for two numbers
    thank you for your attention"""
    if a > b:
        print("The bigger number is ", a)
    elif a == b:
        print("They'r equal ")
    else: 
        print("The bigger number is ", b)
    

findingBiggerNumber(2,2)