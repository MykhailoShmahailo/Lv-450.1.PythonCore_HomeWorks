# 3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)

n = int(input("Enter a number "))
if n == 0: 
    print("Factorial is equal to 1")
elif n < 0:
    print("Factorial doesn't exist")  
else:
    factorial = 1 
    for i in range(2, n+1):
        factorial *= i
    
    print("Factorial is ", factorial)










