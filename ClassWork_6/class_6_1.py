# 1)  Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел. 



def calculating (*args):
    sum = 0
    for value in args:
        sum += value
    return sum / len (args)
    
print(calculating(1,2,3,5,7,4))