number = input("Enter 4 digit number ")
convert = [int(x) for x in str(number)] 
print ("The list from number is " + str(convert)) 

def multiplyList(myList): 
	result = 1
	for x in myList: 
		result = result * x 
	return result 

print("Result", multiplyList(convert))
reversed_list = convert[::-1]
print("Reverse Result ", reversed_list)


def convToInt(reversed_list):      
    s = [str(i) for i in reversed_list]     
    res = int("".join(s))     
    return(res) 
   
print("This is reversed int: ", convToInt(reversed_list))

print("This is sorted number:: ", convToInt(sorted(reversed_list)))