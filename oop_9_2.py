#2.Напишіть програму, яка пропонує користувачу ввести свій вік, 
#після чого виводить повідомлення про те чи вік є парним чи непарним числом. 
#Необхідно передбачити можливість введення від’ємного числа, в цьому випадку 
#згенерувати власну виняткову ситуацію. Головний код має викликати функцію, 
#яка обробляє введену інформацію.

class CustomError(Exception): 
    def __init__(self, data): 
        self.data = data
    def __str__(self):
        return repr(self.data) 

def age ():
    try:
        userNumber = int(input("Enter your age "))
        if userNumber < 0:
            raise CustomError("That is not a positive number!")
        if userNumber == 0:
            raise ValueError("Zero not allowed!")
        if userNumber % 2 == 0:
            print("This age is EVEN - {}".format(userNumber))
        if userNumber % 2 != 0:
            print("This age is ODD - {}".format(userNumber)) 
    except ValueError as e:
        print(e)
    except CustomError as d:
        print(d)    
    finally:
        print("You won!")    

age()        




