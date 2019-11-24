# 4.  Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня, 
# який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) . 
# Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних. item in range

def weeks():
    try:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday","Friday","Saturday","Sunday"]
        numbers = int(input("Enter any number from 1 to 7 "))
        if numbers == 0:
            raise ValueError("Zero not allowed!") 
        if numbers < 0:
            raise ValueError ("Not a positive number")
        if numbers > 7:
            raise ValueError ("Not in range from 1 to 7")
        if numbers == 1:
            print("This is {} day and it called as {}".format(numbers, days[0]))
        if numbers == 2:
            print("This is {} day and it called as {}".format(numbers, days[1]))
        if numbers == 3:
            print("This is {} day and it called as {}".format(numbers, days[2]))    
        if numbers == 4:
            print("This is {} day and it called as {}".format(numbers, days[3]))    
        if numbers == 5:
            print("This is {} day and it called as {}".format(numbers, days[4]))    
        if numbers == 6:
            print("This is {} day and it called as {}".format(numbers, days[5]))    
        if numbers == 7:
            print("This is {} day and it called as {}".format(numbers, days[6]))    

    except ValueError as e:
        print(e)

weeks()        


