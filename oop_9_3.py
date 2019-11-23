# 3.  Напишіть програму для обчислення частки двох чисел, 
# які вводяться користувачем послідовно через кому, 
# передбачити випадок ділення на нуль, випадки синтаксичних помилок 
# та випадки інших виняткових ситуацій. Використати блоки else та finaly.


def place_value(): 
    try:
        number1,number2 = eval(input("Enter any number "))
        if number1 == 0 or number2 == 0:
            raise ValueError ("Zero not allowed!")
        if number1 < 0 or number2 < 0:
            raise ValueError ("Not a positive number")
        else:
            print(number1 / number2)
            print(number2 / number1)
    except ValueError as e:
        print(e)   
    finally:
        print("Have a good day!")        


place_value()
        
        
        
