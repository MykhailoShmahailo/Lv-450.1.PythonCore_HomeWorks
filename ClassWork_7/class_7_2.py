import random


userInput = int(input("Input any number from 1 to 100 "))
randomInput = random.randint(1, 100)
while userInput != randomInput:
    if userInput < randomInput:
        userInput = int(input("Try bigger number "))
    elif userInput > randomInput:
        userInput = int(input("Try smaller number "))
    else:
        print("You Win!")






