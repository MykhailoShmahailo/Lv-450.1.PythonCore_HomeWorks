# 1.  Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.

# myList = []
# numbers = int(input("Enter number of elements : "))
# for c in range(numbers):
#     myList.append(int(input("Entered next number ")))

# print(myList)


new_list = [int(input("Enter number of elements : ")) for x in range(int(input("Entered next number ")))]
print(new_list)

print("Max value is: ", max(new_list))
print("Min value is: ", min(new_list))