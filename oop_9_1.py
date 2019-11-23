# 1.  Напишіть програму, яка пропонує користувачу ввести 
# ціле число і визначає чи це число парне чи непарне, 
# чи введені дані коректні.

def number ():
    try:
        userNumber = int(input("Enter any number "))
        if userNumber < 0:
            raise ValueError("That is not a positive number!")
        if userNumber == 0:
            raise ValueError("Zero not allowed!")
        if userNumber % 2 == 0:
            print("This is EVEN number - {}".format(userNumber))
        if userNumber % 2 != 0:
            print("This is ODD number - {}".format(userNumber)) 
    except ValueError as e:
        print(e)
    finally:
        print("You won!")    

number()        

