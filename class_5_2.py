# 2.  В інтервалі від 1 до 10 визначити числа 
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3, 
# •  числа, які не діляться на 2 та 3.

odd2 = [x for x in range(1,10) if x % 2 == 0 ]
odd3 = [x for x in range(1,10) if x % 3 == 0 and x % 2 != 0]
odd = [x for x in range(1,10) if x % 3 != 0 and x % 2 !=0]
print(odd2)
print(odd3)
print(odd)

#print("Max number - {} Min number - {}", format)
